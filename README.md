## Django-Authentication - A Django Project

Description:

This Django project provides a basic user authentication system, allowing users to register, log in, and log out. Upon successful authentication, users are redirected to the home page.

Prerequisites:

    Python 3.x (https://www.python.org/downloads/)
    pip (usually comes bundled with Python)

Installation:

    Clone the Repository:

    Use Git to clone this repository:
    Bash

    git clone https://github.com/wajidkorkani/Django-Authentication.git

Create a Virtual Environment (Recommended):

It's highly recommended to create a virtual environment to isolate project dependencies. Here's an example using venv:
Bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows

Use code with caution.

Install Dependencies:

Activate your virtual environment. Install the required packages from the requirements.txt file:
Bash

pip install -r requirements.txt


Run Migrations and Create Admin User:

Apply database migrations:
Bash

python manage.py makemigrations
python manage.py migrate

Use code with caution.

Create a superuser for administrative access (replace username, email, and password with your desired values):
Bash

python manage.py createsuperuser 


Running the Project:

    Start the Development Server:

    Run the Django development server:
    Bash

    python manage.py runserver

    This will typically start the server at http://127.0.0.1:8000/ by default.

    Access the Homepage:

    Open your web browser and navigate to http://127.0.0.1:8000/ (or the appropriate URL) to view the application's homepage.

Usage:

    Registration: Use the registration form to create a new user account.
    Login: Authenticate with your existing username and password.
    Logout: Terminate your user session and redirect back to the homepage.