# Creating an Employee Form with CRUD Operation:

 - Create an Virtual Environment	    - python -m venv myenv
 - Activate the Virtual Environment	  - myenv\Scripts\activate
 - Create Django Project		          - django-admin startproject EmployeeAPI
 - Run the Project in server		      - python manage.py runserver
 - Set the Cors Headers			          - In the Settings (Middleware,Installed)
 - Create Django App			            - python manage.py startapp EmployeeApp
 - Register the App 			            - In the Settings (Installed) - 'EmployeeApp.apps.EmployeeappConfig'
 - Start the Code 			              - In the models.py
 - Make Migrations for database		    - python manage.py makemigrations EmployeeApp
 - Complete the Migration	          	- python manage.py migrate EmployeeApp   
 - SQLite Studio		                	- Add and Check the Database  
 - Create Serializers			            - In the App - serializers.py
 - Code					                      - In the views.py
 - Create URLS				                - urls.py in the EmployeeApp
 - Create React				                - npx create-react-app employee_react
 

## Technologies Used:
 - Python
 - Django
 - PostMan
 - SQLite
 - ReactJS
 - ReactBootstrap
