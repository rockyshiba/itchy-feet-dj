To run this project have the latest version of Python installed. 
https://www.python.org/downloads/

Make sure python environment variables are installed with python. If you are unsure, the easiest way is 
to redownload python and check the "install environment vairables" box.

Using a command line interface, cd into the directory containing this project AND the manage.py file then use:
python manage.py runserver

By default Django uses http://127.0.0.1:8000/ locally

Itchy Feet
A prototype social media project with the aim to do CRUD in Django. Some design decisions don't make sense at this
stage of the project but as it stands currently CRUD is possible. 
To demonstrate this for yourself, create a new user using Sign Up. Then login using Login with email and password. 

The heart of the project is in the register directory. 
The models are in models.py
the controllers are in views.py
the views are in the templates/register directory
the url routes are in urls.py

The admin is at http://127.0.0.1:8000/admin 

Outputing images to the front end is currently a mystery for myself. 

Google Maps api
The locations are database driven using geocoder web service. 
The arguments provided are users' current locations provided by their profiles. 
Users will blank current locations are skipped in the array. 
The javascript logic is in the templates/register directory as homepage.html. 

