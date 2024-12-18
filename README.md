# Quiz App Django

A Django-based web application for conducting quizzes.

## Prerequisites

Ensure you have the following installed on your system:

- Python (version 3.7 or higher)
- pip (Python package installer)
- Git

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohdshubair313/quiz_app_django.git
   cd quiz_app_django
2. **Create and activate a virtual environment:**
 ```bash
python -m venv env
.\env\Scripts\activate

3. **Install the required packages:**
 ```bash
pip install -r requirements.txt

4. **Apply database migrations:**
  python manage.py migrate

5 **Create a superuser (for accessing the Django admin interface):**
   python manage.py createsuperuser

6. **Run the development server:**
python manage.py runserver

Usage
Navigate to http://127.0.0.1:8000/ to access the quiz application.
To access the Django admin interface, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
