from django.contrib import admin
from djoi.authors.models import Author, Alias
from djoi.publications.models import Publication

admin.site.register(Author)

class AliasAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', ]
    
    def get_queryset(self, request):
        return super(AliasAdmin,self).get_queryset(request).select_related('author')

admin.site.register(Alias, AliasAdmin)
admin.site.register(Publication)