from django.db import models
from django.template.defaultfilters import slugify
from djoi.authors.models import Author
from djoi.staff.models import Employee, Alias
from django.db.models import Q

from crossref.restful import Works
works = Works()

class PublicationManager(models.Manager):
    
    def by_name(self, name):
        author = Author.objects.filter(name=name).first() or None
        if author:
            return super(PublicationManager, self).filter(author__name__contains=name)
        else:
            return super(PublicationManager, self)
    
    def by_employee(self, employee):
        q_objects = Q(author__name__contains=employee.name)
        for alias in employee.alias_set.all():
            q_objects |= Q(author__name__contains=alias.name)
        return Publication.objects.filter(q_objects)

class Publication(models.Model):
    doi = models.CharField(max_length=63, blank=False)
    title = models.CharField(max_length=255, blank=True)
    author = models.ManyToManyField(Author, blank=True)
    citation = models.TextField(null=False, default='Not available')
    
    def __str__(self):
        return self.doi

    def __repr__(self):
        return str(self.doi)

    def save(self, *args, **kwargs):
        work = works.doi(doi=self.doi)
        self.title = work['title'][0]
        super(Publication, self).save(*args, **kwargs)

    objects = PublicationManager()
    by_names = PublicationManager()