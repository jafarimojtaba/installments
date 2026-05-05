# Backend API

Django REST API for the Money Tracker application.

## Tech Stack

- Django 6.0.4
- Django REST Framework
- Simple JWT (Cookie-based authentication)
- SQLite (development)

## Setup

1. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run development server:
```bash
python manage.py runserver
```

## API Endpoints

- `POST /api/token/` - Login (returns JWT cookie)
- `GET /api/installments/` - List user's installments
- `POST /api/installments/` - Create new installment
- `GET /api/installments/{id}/` - Get specific installment
- `PUT/PATCH /api/installments/{id}/` - Update installment
- `DELETE /api/installments/{id}/` - Delete installment

## Project Structure

```
backend/
├── config/              # Django project settings
├── core/                # Shared authentication and utilities
├── installments/        # Installments app
│   ├── services/        # Business logic
│   ├── utils/          # App-specific utilities
│   └── constants/      # App-specific constants
├── manage.py
└── requirements.txt
```
