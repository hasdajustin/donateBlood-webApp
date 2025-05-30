# DonateBlood Web App

A Django-based web application that helps users register as blood donors, search for available donors, and manage blood donation records.

## Features

- User Registration and Login
- Donor Profile Creation
- Donor Search by Blood Group and Location
- Admin Dashboard to Manage Users and Donors
- Dynamic Forms with Django Widget Tweaks

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Tools:** python-dotenv, django-widget-tweaks

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` (Python package installer)

### Installation Steps

1. **Clone the project:**

    ```bash
    git clone https://github.com/hasdajustin/donateBlood-webApp
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    venv\Scripts\activate       # For Windows
    # source venv/bin/activate  # For macOS/Linux
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the site:**

    Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Environment Variables

You need to create a `.env` file in the root folder of your Django project and store important variables like SECRET_KEY inside it
