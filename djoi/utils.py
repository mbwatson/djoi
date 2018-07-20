from djoi.authors.models import Author, Alias
from djoi.publications.models import Publication

def findKnownAuthor(author):
    first_name = author['given']
    last_name = author['family']
    known_author = Author.objects.by_name(first_name, last_name).first() or None
    known_alias = Alias.objects.filter(name=f'{first_name} {last_name}').first() or None
    if known_author:
        return known_author
    elif known_alias:
        return known_alias.author
    else:
        return {
            'first_name': author['given'],
            'last_name': author['family'],
            'full_name': f'{author["given"]} {author["family"]}',
        }

def getAuthors(authors):
    author_objects = []
    for author in authors:
        known_author = findKnownAuthor(author)
        author_objects.append(known_author)
    return author_objects

def publicationObject(work):
    return_publication = {
        'doi': work['DOI'],
        'title': work['title'][0],
        'authors': getAuthors(work['author']),
    }
    return return_publication

