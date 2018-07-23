from django.shortcuts import render, get_list_or_404
from djoi.publications.models import Publication
from djoi.staff.models import Employee

def index(request):
    publications = get_list_or_404(Publication)
    staff = get_list_or_404(Employee)
    context = {
        'publications': publications,
        'staff': staff,
    }
    return render(request, 'djoi/index.html', context)