from django.contrib import admin
from djoi.authors.models import Author, Alias
from djoi.publications.models import Publication
from djoi.utils import getAuthors

from crossref.restful import Works
works = Works()

#

admin.site.register(Author)

#

class AliasAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', ]
    
    def get_queryset(self, request):
        return super(AliasAdmin,self).get_queryset(request).select_related('author')

admin.site.register(Alias, AliasAdmin)

#

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('doi', 'title')
    # exclude = ('author', 'title')

    def save_related(self, request, form, formsets, change):
        super(PublicationAdmin, self).save_related(request, form, formsets, change)
        work = works.doi(doi=form.instance.doi)
        authors = [obj for obj in getAuthors(work['author']) if type(obj) is Author]
        for author in authors:
            form.instance.author.add(author)

admin.site.register(Publication, PublicationAdmin)
