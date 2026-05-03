# Installments API

A Django REST API for tracking installment payments with JWT authentication.

## Features

- JWT authentication with cookie-based tokens
- Track installment payments with calculated fields:
  - [total_paid](cci:1://file:///Users/mjpro/Desktop/projects/installments/installments/models.py:12:4-20:24) - Amount paid to date
  - [remaining_amount](cci:1://file:///Users/mjpro/Desktop/projects/installments/installments/models.py:11:4-13:49) - Balance remaining
  - [remaining_months](cci:1://file:///Users/mjpro/Desktop/projects/installments/installments/models.py:8:4-10:80) - Months left to pay
  - [last_payment_date](cci:1://file:///Users/mjpro/Desktop/projects/installments/installments/models.py:18:4-20:62) - Final payment date
  - [progress_percentage](cci:1://file:///Users/mjpro/Desktop/projects/installments/installments/models.py:22:4-24:64) - Payment progress
  - [is_paid](cci:1://file:///Users/mjpro/Desktop/projects/installments/installments/models.py:26:4-28:50) - Payment completion status
- User-specific data isolation
- CORS enabled for frontend integration

## Setup

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate