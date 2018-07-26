from django.db import models
from django.template.defaultfilters import slugify
from djoi.models.staff import Alias
from django.db.models import Q
from djoi.utils import getCitation
from crossref.restful import Works

works = Works()

# Authors

class AuthorManager(models.Manager):
    def create_author(self, name):
        author = self.create(name=name)
        return author

class Author(models.Model):
    name = models.CharField(max_length=127, blank=False, unique=True)

    def __str__(self):
        return self.name

    @property
    def alias(self):
        alias = Alias.objects.filter(name=self.name).first() or None
        return alias

    @property
    def slug(self):
        alias = self.alias
        if alias is not None:
            return alias.slug
        else:
            return None

    objects = AuthorManager()

# Publications

class PublicationManager(models.Manager):
    
    def create_publication(self, doi):
        publication = self.create(doi=doi)
        return publication

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
    doi = models.CharField(max_length=63, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=True)
    author = models.ManyToManyField(Author, blank=True)
    citation = models.TextField(blank=True, null=False, default='Not available')

    def __str__(self):
        return self.doi

    def __repr__(self):
        return str(self.doi)

    def save(self, *args, **kwargs):
        work = works.doi(doi=self.doi)
        self.title = work['title'][0]
        self.citation = getCitation(self.doi)
        super(Publication, self).save(*args, **kwargs)

    objects = PublicationManager()
    by_names = PublicationManager()

