from django.db import models
from django.contrib.auth.models import User
from datetime import date
from calendar import monthrange

class Installment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_amount = models.DecimalField(max_digits=10, decimal_places=2)

    purchase_date = models.DateField()
    first_payment_date = models.DateField()

    pay_day = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.total_paid}"

    @property
    def total_paid(self):
        today = date.today()

        first_due = self.first_payment_date
        if first_due > today:
            return self.monthly_amount * 0

        months_count = 0
        due = first_due
        while due <= today:
            months_count += 1

            if due.month == 12:
                year = due.year + 1
                month = 1
            else:
                year = due.year
                month = due.month + 1

            last_day = monthrange(year, month)[1]
            day = min(self.pay_day, last_day)
            due = date(year, month, day)

        return self.monthly_amount * months_count
    
    @property
    def remaining_amount(self):
        return self.total_price - self.total_paid
    
    @property
    def remaining_months(self):
        return round((self.total_price - self.total_paid) / self.monthly_amount)
    @property
    def last_payment_date(self):
        months = self.remaining_months
        year = self.first_payment_date.year
        month = self.first_payment_date.month + months
        
        # Adjust year if month exceeds 12
        while month > 12:
            month -= 12
            year += 1
        
        # Clamp day to last day of target month
        last_day = monthrange(year, month)[1]
        day = min(self.first_payment_date.day, last_day)
        
        return date(year, month, day)
        
    @property
    def progress_percentage(self):
        return round((self.total_paid / self.total_price) * 100)

    @property
    def is_paid(self):
        return self.total_paid >= self.total_price
    
    
