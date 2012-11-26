multipart-form-data_django_rest_framework_tutorial
======================================

About
----------

date: 2012/11/25

This is a simple django-rest-framework multipart/form-data example.

Requirements
--------------

Setup was on ubuntu 12.04.

	*Django==1.4.2
	*Pygments==1.5
	*argparse==1.2.1
	*djangorestframework==2.1.6
	*wsgiref==0.1.2
	*requests==0.14.2a

Installation and setup
---------------

1. Download and cd into the multipart-form-data_django_rest_framework_tutorial:
    
    ``$ cd multipart-form-data_django_rest_framework_tutorial/``

2. Install requirements from the r.txt file with pip:

    ``$ pip install -r requirements.txt``
    
3. Setup database:
    
    ``$ python manage.py sncdb``
    
4. Run the Django development server:
    
    ``$ python manage.py runserver``
    

Uploading files
---------------

This files provides commands to upload files to the django-rest-framework api. 

1.	Open a python interpreter:

	``$ python``

2.	Import requests in python interpreter:

	``$import requests``
	
3. Swap out the YOUR_URL in the url variables with your root url:

	``$url_upload_form = 'YOUR_URL/api/upload_form/'``

	``$url_upload_serializers = 'YOUR_URL/api/upload_serializers/'``
	
4. Paste url variables into python interpreter:

5. Create a file to up:

	``$files = {'docfile': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}``
	
6. Upload a file with a form:

	``$r=requests.post(url_upload_form, data={'title':'file_upload_form'}, files=files)``
	
7. Upload a file with django-rest-framework serializer:

	``$r=requests.post(url_upload_serializers, data={'title':'file_upload_serializers'}, files=files)``

8. To view uploaded data in the django-rest-framework view go to:

	``$YOUR_URL/api/upload_form/``
	
	or 
	
	``$YOUR_URL/api/upload_serializers/``



	

	

	



