from django.db import models
from django.template.defaultfilters import slugify

class AuthorManager(models.Manager):
    def create_author(self, name):
        author = self.create(name=name)
        return author


class Author(models.Model):
    name = models.CharField(max_length=127, blank=False)
    slug = models.SlugField(max_length=255, editable=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    objects = AuthorManager()
