from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template.defaultfilters import slugify
from djoi.utils import publicationObject
from crossref.restful import Works
from djoi.models.publications import Publication, Author
from djoi.models.staff import Employee, Alias

from django.http import HttpResponse

works = Works()

# Publication Views

def publicationList(request):
    try:
        publications = Publication.objects.all()
    except Publication.DoesNotExist:
        publications = []
    context = {
        'publications': publications
    }
    return render(request, 'djoi/publicationList.html', context)

# Staff Views

def staffList(request):
    try:
        staff = Employee.objects.all()
    except Employee.DoesNotExist:
        staff = []
    context = {
        'staff': staff,
    }
    return render(request, 'djoi/staffList.html', context)

    # lookup_names = [employee.name]
    # for alias in employee.alias_set.all():
    #     lookup_names.append(alias.name)

def staffDetail(request, employee_slug):
    employee = get_object_or_404(Employee, slug=employee_slug)
    publications = Publication.objects.by_employee(employee)
    context = {
        'author': employee,
        'publications': publications,
    }
    return render(request, 'djoi/staffDetail.html', context)

# Main View

def index(request):
    try:
        staff = Employee.objects.all()
        publications = Publication.objects.all()
    except Employee.DoesNotExist:
        staff = []
        publications = []
    context = {
        'publications': publications,
        'staff': staff,
    }
    return render(request, 'djoi/index.html', context)

