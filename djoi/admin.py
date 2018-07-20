from django.contrib import admin
from djoi.authors.models import Author
from djoi.publications.models import Publication
from djoi.staff.models import StaffMember, Alias
from djoi.utils import getAuthors

from crossref.restful import Works
works = Works()

#

admin.site.register(Author)

#

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('doi', 'title')
    # exclude = ('author', 'title')

    def save_related(self, request, form, formsets, change):
        super(PublicationAdmin, self).save_related(request, form, formsets, change)
        work = works.doi(doi=form.instance.doi)
        for author in work['author']:
            # remove incorrectly assigned authors?
            author_full_name = f'{author["given"]} {author["family"]}'
            if Author.objects.filter(name=author_full_name).exists():
                author = Author.objects.get(name=author_full_name)
            else: 
                author = Author.objects.create_author(author_full_name)
            form.instance.author.add(author)

admin.site.register(Publication, PublicationAdmin)

#

admin.site.register(StaffMember)

class AliasAdmin(admin.ModelAdmin):
    list_display = ['name', 'staff_member', ]
    
    def get_queryset(self, request):
        return super(AliasAdmin,self).get_queryset(request).select_related('staff_member')

admin.site.register(Alias, AliasAdmin)

