from djoi.authors.models import Author, Alias
from djoi.publications.models import Publication

def getAuthors(authors):
    author_objects = []
    wanted_keys = ['given', 'family']
    for author in authors:
        alias = Alias.objects.filter(name=f'{author["given"]} {author["family"]}').first() or None
        if alias:
            author_objects.append(alias.author)
        else:
            known_author = Author.objects.by_name(author['given'], author['family']).first() or None
            if known_author:
                author_objects.append(known_author)
    return author_objects

def publicationObject(work):
    return_publication = {
        'doi': work['DOI'],
        'title': work['title'][0],
        'authors': getAuthors(work['author']),
    }
    return return_publication

