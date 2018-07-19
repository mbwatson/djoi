from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Publication
from djoi.authors.models import Author, Alias
from djoi.utils import publicationObject

from crossref.restful import Works
works = Works()

def publications(request):
    publications = []
    dois = get_list_or_404(Publication)
    dois = [doi.doi for doi in dois]
    for doi in dois:
        work = works.doi(doi=doi)
        publications.append(publicationObject(work))
    context = {
        'publications': publications
    }
    return render(request, 'djoi/publications.html', context)