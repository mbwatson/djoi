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

class AliasManager(models.Manager):
    def by_employee(self, employee):
        return super(AliasManager, self).filter(employee=employee)

class Alias(models.Model):
    name = models.CharField(max_length=127, blank=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    objects = AliasManager()
    by_employee = AliasManager()

    class Meta:
        verbose_name_plural = 'Aliases'
