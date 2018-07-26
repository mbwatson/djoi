import requests

def getAuthors(authors):
    author_objects = []
    for author in authors:
        author_objects.append(findStaffAuthor(author) or { 'name': f'{author["family"]} {author["given"]}', })
    return author_objects

def publicationObject(work):
    return_publication = {
        'doi': work['DOI'],
        'title': work['title'][0],
        'authors': getAuthors(work['author']),
    }
    return return_publication

def getCitation(doi, citation_format='apa'):
    url = f'https://search.crossref.org/citation?format={citation_format}&doi={doi}'
    citation = requests.get(url)
    citation.encoding = 'utf-8'
    return citation.text or None