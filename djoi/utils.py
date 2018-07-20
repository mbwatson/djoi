from djoi.authors.models import Author
from djoi.publications.models import Publication
from djoi.staff.models import StaffMember, Alias

def findStaffAuthor(author):
    first_name = author['given']
    last_name = author['family']
    name = f'{first_name} {last_name}'
    staff_author = StaffMember.objects.by_name(first_name, last_name).first() or None
    staff_alias = Alias.objects.filter(name=name).first() or None
    if staff_author:
        return staff_author
    elif staff_alias:
        return {
            'name': staff_alias.name,
            'slug': staff_alias.staff_member.slug,
        }
    else:
        return None

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

