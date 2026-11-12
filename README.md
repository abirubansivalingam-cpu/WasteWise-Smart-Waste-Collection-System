# WasteWise – Smart Waste Collection Management System

A Django-based MCA full-stack project for managing community waste pickup requests, collection status, schedules, staff, vehicles, complaints and operational reports.

## Features
- Authentication: registration, login, logout and profile
- Dashboard with request KPIs and Chart.js visualisations
- Create and track waste collection requests
- Request status workflow (staff/admin users)
- Pickup schedule, staff directory and fleet overview
- Community complaint submission and review
- Reports and CSV export
- Django admin management
- Responsive forest-green UI for desktop and mobile
- SQLite default; PostgreSQL configuration included

## Requirements
- Python 3.10+ (Python 3.14 is suitable)
- pip
- Optional: PostgreSQL 15+

## Windows CMD setup
```bat
cd %USERPROFILE%\Downloads\WasteWise_MCA_Project
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations operations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```
Open http://127.0.0.1:8000/

Demo user after `seed_demo`:
- Username: `waste_demo`
- Password: `WasteWise@123`

Change the demo password before any real deployment. Create a separate superuser for admin at `/admin/`.

## PostgreSQL configuration (optional)
Create database `wastewise_db`, then set environment variables in CMD:
```bat
set DB_ENGINE=postgres
set DB_NAME=wastewise_db
set DB_USER=postgres
set DB_PASSWORD=YOUR_POSTGRES_PASSWORD
set DB_HOST=localhost
set DB_PORT=5432
python manage.py migrate
```
Install the requirements first. SQLite is used unless `DB_ENGINE=postgres`.

## Run tests
```bat
python manage.py test
python manage.py check
```

## Important notes
- Collection schedule, staff, and vehicle records can be added through Django admin.
- The initial release does not integrate live GPS, SMS/email gateways, municipal APIs, or payment services.
- The charts use Chart.js from a CDN, so an internet connection is needed for chart rendering.
- Before production: set a strong `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=0`, configure `DJANGO_ALLOWED_HOSTS`, use HTTPS, review permissions, and configure backups.
