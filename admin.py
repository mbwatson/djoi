from django.contrib import admin
from djoi.models.publications import Publication, Author
from djoi.models.staff import Employee, Alias
from djoi.utils import getAuthors

from crossref.restful import Works
works = Works()

#

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Author, AuthorAdmin)

#

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('doi', 'title')
    exclude = ('author', 'title', 'citation')
    
    def save_related(self, request, form, formsets, change):
        super(PublicationAdmin, self).save_related(request, form, formsets, change)
        work = works.doi(doi=form.instance.doi)
        form.instance.author.clear()
        for author in work['author']:
            ''' Empty strings given as defaults here becuase we don't know if both
            given and family names are provided.'''
            author_full_name = f'{author.get("given", "")} {author.get("family", "")}'
            if Author.objects.filter(name=author_full_name).exists():
                author = Author.objects.get(name=author_full_name)
            else: 
                author = Author.objects.create_author(author_full_name)
            form.instance.author.add(author)

admin.site.register(Publication, PublicationAdmin)

admin.site.register(Employee)

#

class AliasAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('employee', 'name',)
        }),
    )

admin.site.register(Alias, AliasAdmin)
