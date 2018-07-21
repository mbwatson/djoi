from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Publication
from djoi.authors.models import Author
from djoi.utils import publicationObject

from crossref.restful import Works
works = Works()

def publications(request):
    publications = get_list_or_404(Publication)
    context = {
        'publications': publications
    }
    return render(request, 'djoi/publications/index.html', context)