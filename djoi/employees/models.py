from django.db import models
from django.template.defaultfilters import slugify

class Employee(models.Model):
    first_name = models.CharField(max_length=127, blank=False)
    last_name = models.CharField(max_length=127, blank=False)
    slug = models.SlugField(max_length=255, editable=False, unique=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Employee, self).save(*args, **kwargs)

    objects = AuthorManager()
