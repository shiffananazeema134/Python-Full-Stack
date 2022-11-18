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
 - Start React                              - npm start
 - Get ReactBootstrap
 

## Technologies Used:
 - Python
 - Django
 - PostMan
 - SQLite
 - ReactJS
 - ReactBootstrap

 Object-Oriented Programming (OOPS)

Principles of OOPS:
Class                      -  collection of objects
Object                    -  entity that has state and behavior
Method                  -  functions defined inside a class
Inheritance            -  creating new class from existing class    - Person -> child, friend, student
Polymorphism      -  perform a single action in different ways  - Duck -> fly, walk, swim
Encapsulation      -  restrict access to some objects  -  public, private, protected 
Abstraction           -  only showing relevant data          - car starts by key, no need to know h
