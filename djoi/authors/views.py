from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Author
from djoi.publications.models import Publication
from djoi.utils import publicationObject

from crossref.restful import Works
works = Works()

def authors(request):
    authors = get_list_or_404(Author)
    context = {
        'authors': authors,
    }
    return render(request, 'djoi/authors.html', context)

def author(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    publications = []
    dois = author.publication_set.all()
    for doi in dois:
        work = works.doi(doi=doi.doi)
        publications.append(publicationObject(work))
    context = {
        'author': author,
        'publications': publications,
    }
    return render(request, 'djoi/author.html', context)
