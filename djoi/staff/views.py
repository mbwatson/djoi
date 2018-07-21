from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Employee
from djoi.publications.models import Publication
from djoi.staff.models import Employee

def index(request):
    staff = get_list_or_404(Employee)
    context = {
        'staff': staff,
    }
    return render(request, 'djoi/staff/index.html', context)

def detail(request, employee_slug):
    employee = get_object_or_404(Employee, slug=employee_slug)
    context = {
        'author': employee,
    }
    return render(request, 'djoi/staff/detail.html', context)
