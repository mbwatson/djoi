# DjOI

### Django Object Identifier

This is a simple Django app that makes use of [Crossref Rest API](https://github.com/CrossRef/rest-api-doc) to build a relationship between a group of people (say, staff members of an organization) and their publications along with their citations based on a list of DOIs (Digital Object Identifiers).

### Installation

Clone this repository into the root of your project. This is the directory that holds the `manage.py` file.

You'll need to add djoi to your project's installed apps in `settings.py`

```python
  INSTALLED_APPS = [
    ...
    'djoi',
  ]
```

and point DjOI-related urls to the DjOI app's urls file by adding 

```python
urlpatterns = [
    ...
    path('djoi/', include('djoi.urls')),
]
```
to your project's `urls.py` file. Be sure the top of your project's `urls.py` has a line that looks like the following.

```python
from django.urls import path, include`
```

Otherwise you will receive the error  `name 'include' is not defined` because then you have called, but not imported, `include` from the `django.urls` module.

Now, let's add the necessary tables by executing the following commands.

```bash
$ python3 manage.py makemigrations
```

and

```bash
$ python3 manage.py migrate
```

Make sure your development server is up and running. If not, execute

```bash
$ python3 manage.py runserver`
```

Point your browser at `localhost:8000/djoi` to see a fairly plain welcome page with some links to a Publications page and a Staff page, both of which are empty initially.

### The API

The content of the tables are accessible in your templates ina  fairly straight-forward manner.

##### The Employee Model

An `Employee` object `employee` consists of `employee.first_name`, `employee.last_name`, `employee.name`, and `employee.slug`. Each employee's aliases are accessible as a queryset via `employee.alias_set` in your template, and you can apply normal queryset mthods, such as `first` and `all`.

##### The Alias Model

The `Alias` model is quite simple, and it's only purpose is the bridge between publications' authors and your staff list. An `Alias` object `alias` knows its name through `alias.name`, and it knows the employee for which it is an alias via `alias.employee`.

##### The Publication Model

The `Publication` model knows its DOI `publication.doi`, its title `publication.title`, its citation `publication.citation`, and queryset of set of authors `publication.author`, and you can apply normal queryset mthods, such as `first` and `all`.

Note that the publication's DOI is used to link to the permanent location of the document online: `https://doi.org/{{ publication.doi }}`.

##### The Author Model

An `Author` object `author` is simply a name, accessed with `author.name`, that knows the alias object it is related to (provided it *is* in fact related to one) via `author.alias`. If it is indeed related to an alias, then it is related to a coreesponding author, as well. Thus the `author` objects knows the slug which will take you to the author's page, `author.slug`.

### How to Use: An Example

##### With the Admin UI

For the sake of having an instructional exmaple, suppose your organization has two staff members: Richard Stanley and Bruce Sagan (two of my favorite mathematicians). In the Django Admin panel, add these two employees by entering their first and last names.

Now, upon navigating to the staff page at `localhost:8000/djoi/staff`, you'll find those staff members. Clicking on each of their names takes you to a dynamically rendered page that displays his publications. Let's change that by adding some publications.

Head back to Publications in the admin panel, and add a few publications by entering the following DOIs one-at-a-time and pressing the Save button:

`10.1017/cbo9781139004114.006` and `10.1016/0097-3165(90)90066-6`.

Head back to the Publications page again, and there they should be. You'll even notice that the DjOI app identified the titles and citations of the publications. Moreover, it found the authors in your Staff list who authored those publications, and Bruce Sagan will have a link to his page.

You will notice a problem: Bruce Sagan's name is *not* linked in the other publication's author list. That's because his name appears differently in that publication's meta data. Therefore, we will have to give him and alias so DjOI knows they are simply two names for the same person.

In the Admin panel, we'll add an alias. Press the Add Employee Alias button, choose Bruce Sagan from the list of employees, and enter `Bruce E Sagan` as the alias.

Head back to view the publications list and author's page to see the publications' author lists populated with links. All links point to the original author's page with a slug, e.g., `bruce-sagan` in thise case.

##### With the Shell

You can, of course, test the saved information by opening up a shell with `python3 manage shell` in your project's root directory and importing the models from the DjOI module with the following commands.

```pycon
>>> from djoi.staff.models import Employee, Alias
>>> from djoi.publications.models import Publication, Author
```

Some basic commands and their results follow.

```pycon
>>> employee.alias_set.all()
<QuerySet [<Alias: Bruce Sagan>, <Alias: Bruce E. Sagan>]>

>>> employee = Employee.objects.first()
<Employee: Bruce Sagan>

>>> employee.alias_set.all()
<QuerySet [<Alias: Bruce Sagan>, <Alias: Bruce E. Sagan>]>

>>> alias = employee.alias_set.all()[0]
<Alias: Bruce Sagan>

>>> alias.employee
<Employee: Bruce Sagan>

>>> publication = Publication.objects.last()
>>> publication
10.1016/0097-3165(90)90066-6

>>> publication.doi
'10.1016/0097-3165(90)90066-6'

>>> publication.citation
'Sagan, B. E., & Stanley, R. P. (1990). Robinson-schensted algorithms for skew tableaux. Journal of Combinatorial Theory, Series A, 55(2), 161–193. doi:10.1016/0097-3165(90)90066-6'

>>> publication.author.all()
<QuerySet [<Author: Bruce E Sagan>, <Author: Richard P Stanley>]>

>>> publication.author.filter(name='Charlie Brown')
<QuerySet []>

>>> publication.author.filter(name='Bruce E Sagan')
<QuerySet [<Author: Bruce E Sagan>]>

>>> author = publication.author.first()
>>> author
<Author: Bruce E. Sagan>

>>> author.alias
<Alias: Bruce E. Sagan>

>>> author.alias.slug
'bruce-sagan'

```