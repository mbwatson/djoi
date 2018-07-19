from django.contrib import admin
from .models import Author, Alias, Publication

admin.site.register(Author)

class AliasAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', ]
    
    def get_queryset(self, request):
        return super(AliasAdmin,self).get_queryset(request).select_related('author')

admin.site.register(Alias, AliasAdmin)
admin.site.register(Publication)