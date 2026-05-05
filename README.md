# Money Tracker

Full-stack application for tracking installment payments with JWT authentication.

## Project Structure

```
money_tracker/
├── backend/                 # Django REST API
│   ├── config/             # Django project settings
│   ├── core/               # Shared authentication & utilities
│   ├── installments/       # Installments app
│   │   ├── services/       # Business logic
│   │   ├── utils/          # App-specific utilities
│   │   └── constants/      # App-specific constants
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js app router
│   │   ├── components/    # Reusable UI components
│   │   ├── lib/          # Utility functions, API clients
│   │   ├── hooks/        # Custom React hooks
│   │   └── types/        # TypeScript types
│   └── README.md
├── docker-compose.yml
└── README.md
```

## Features

- JWT authentication with cookie-based tokens
- Track installment payments with calculated fields:
  - Total paid to date
  - Remaining balance
  - Months left to pay
  - Final payment date
  - Payment progress percentage
  - Payment completion status
- User-specific data isolation
- CORS enabled for frontend integration

## Quick Start

### Using Docker Compose (Recommended)

```bash
docker-compose up
```

### Manual Setup

**Backend:**
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend:**
```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

## Documentation

- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)