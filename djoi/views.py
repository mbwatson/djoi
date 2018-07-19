from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Author, Alias, Publication
from django.utils.http import urlunquote

from crossref.restful import Works
works = Works()

def authors(request):
    authors = get_list_or_404(Author)
    context = {
        'authors': authors,
    }
    return render(request, 'djoi/authors.html', context)

def authorList(authors):
    author_objects = []
    wanted_keys = ['given', 'family']
    for author in authors:
        author_object = { key: author[key] for key in wanted_keys } # Copy incoming authors, but only the wanted keys
        author_object['full_name'] = f'{author["given"]} {author["family"]}'
        alias = Alias.objects.filter(name=author_object['full_name']).first() or None
        if alias:
            author_object['slug'] = alias.author.slug
        else:
            authors_in_db = Author.objects.by_name(author['given'], author['family']) or None
            if authors_in_db:
                author_object['slug'] = authors_in_db[0].slug
        author_objects.append(author_object)
    return author_objects

def publicationObject(work):
    return_publication = {
        'doi': work['DOI'],
        'title': work['title'][0],
        'authors': authorList(work['author']),
    }
    return return_publication

def author(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    aliases = author.aliases
    dois = author.publication_set.all()
    publications = []
    for doi in dois:
        work = works.doi(doi.doi)
        publications.append(publicationObject(work))
    context = {
        'author': author,
        'aliases': aliases,
        'dois': dois,
        'publications': publications,
    }
    return render(request, 'djoi/author.html', context)

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