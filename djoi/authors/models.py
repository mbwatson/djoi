from django.db import models
from django.template.defaultfilters import slugify

class AuthorManager(models.Manager):
    def by_name(self, first_name, last_name):
        return super(AuthorManager, self).filter(first_name=first_name, last_name=last_name)

class Author(models.Model):
    first_name = models.CharField(max_length=127, blank=False)
    last_name = models.CharField(max_length=127, blank=False)
    slug = models.SlugField(max_length=255, editable=False, unique=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('last_name', 'first_name')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name} {self.last_name}')
        super(Author, self).save(*args, **kwargs)

    @property
    def aliases(self):
        return Alias.objects.by_author(self)

    objects = AuthorManager()
    filter_by_name = AuthorManager()

class AliasManager(models.Manager):
    def by_author(self, author):
        return super(AliasManager, self).filter(author=author)

class Alias(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=127, blank=False)

    def __str__(self):
        return self.name

    objects = AliasManager()
    by_author = AliasManager()

    class Meta:

        verbose_name_plural = 'Aliases'
