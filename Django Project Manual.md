Django Project Manual:-
API for Managing Users, Clients, and Projects

Table of Contents

1.Project Overview

2.Prerequisites

3.Installation and Setup

4.Database Configuration

5.Running the Project

6.API Endpoints

7.Testing the API

8.Troubleshooting

9.Conclusion

1> Project Overview:

This project is a Django-based API for managing users, clients, and projects. It allows users to create and manage clients, add new projects for those clients, and assign users to projects.

2>Prerequisites:

Before you begin, ensure you have the following installed:

Python 3.6 or higher
pip (Python package installer)
PostgreSQL (or MySQL, depending on your database choice)
Django (version 3.2 or higher)
Django REST Framework (version 3.12 or higher)
psycopg2 (PostgreSQL adapter for Python, if using PostgreSQL)

3> Installation and Setup:

Clone the Repository

bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Create a Virtual Environment

bash
python -m venv env
Activate the Virtual Environment

On Windows:
bash
.\env\Scripts\activate

On macOS/Linux:
bash
source env/bin/activate 
Install Required Packages:
bash
pip install -r requirements.txt
Database Configuration
Create a PostgreSQL/MySQL Database

Create a database using your database management tool or command line.

4> Configure Database Settings:

Open settings.py in your Django project.

Configure the DATABASES setting with your database credentials:
python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',  # or '3306' for MySQL
    }
}

Migrate Database

bash
python manage.py migrate

5> Running the Project:  

Start the Development Server

bash
python manage.py runserver
Access the API Open your web browser or API client (like Postman) and navigate to:

arduino
http://127.0.0.1:8000/

6> API Endpoints:

Authentication
Login: /api/auth/login/
Logout: /api/auth/logout/
User Management
Create User: POST /api/users/
Get User: GET /api/users/<id>/
Update User: PUT /api/users/<id>/
Delete User: DELETE /api/users/<id>/

Client Management:

Create Client: POST /api/clients/
Get Client: GET /api/clients/<id>/
Update Client: PUT /api/clients/<id>/
Delete Client: DELETE /api/clients/<id>/

Project Management:

Create Project: POST /api/projects/
Get Project: GET /api/projects/<id>/
Update Project: PUT /api/projects/<id>/
Delete Project: DELETE /api/projects/<id>/

7> Testing the API:

You can test the API using tools like Postman or cURL. For example, to create a new user, you can send a POST request to /api/users/ with the user details in the request body.

* Example cURL Command
bash
curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{"username": "newuser", "password": "yourpassword"}'

8>Troubleshooting:

Error: ImportError: DLL load failed while importing _psycopg: Ensure you have psycopg2 installed correctly. You might need to reinstall it:

bash
pip uninstall psycopg2
pip install psycopg2-binary
404 Error: Check the URL and ensure the endpoints match those defined in your urls.py.

9> Conclusion:

This manual provides a comprehensive guide to set up, run, and test your Django project API for managing users, clients, and projects. For further assistance, refer to the Django and Django REST Framework documentation.
