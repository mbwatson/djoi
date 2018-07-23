# DjOI

This is a [https://www.djangoproject.com/](Django) project for integrating a staff list with publications by corss-referencing the authors listed according to the publcations' DOIs.

## Getting Started

If you are using this, you will likely require some customization or integration with a current Django project, so these instructions will get you up and running with a development server.

### Prerequisites

First, be sure you have Python and Django installed on your system.

`apt-get install python3`

`pip3 install Django==2.0.7`

The data gathered by this tool is through the [https://github.com/CrossRef/rest-api-doc](Crossref REST API) with the [https://github.com/fabiobatalha/crossrefapi](Crossref API Client) library for python.

`pip3 install crossrefapi`

### Installing

Clone this repository.

`git clone https://github.com/renciweb/djoi.git`

Setup database (sqlite3).

`python3 manage.py makemigrations`

`python3 manage.py migrate`

Create super user.

`python3 manage.py createsuperuser`.

Start the server.

`python3 manage.py runserver`

Point your browser to `localhost:8000` to see the site.
Point your browser to `localhost:8000/admin` to see the administrative backend.

## Using Djoi

Add DOIs in the dministrative panel, and the crossref API will be probed for authors and citations. You also build out a list of employees in the admin panel, and a small site of linked pages will be built to puruse in your browser, acessible at `localhost:8000` while Django runs in development mode.