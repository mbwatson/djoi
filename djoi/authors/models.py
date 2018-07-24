from django.db import models
from django.template.defaultfilters import slugify
from djoi.staff.models import Employee, Alias

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
