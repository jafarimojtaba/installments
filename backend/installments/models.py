from django.db import models
from django.contrib.auth.models import User
from .services.installment_calculations import InstallmentCalculator


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
        return InstallmentCalculator.calculate_total_paid(self)
    
    @property
    def remaining_amount(self):
        return InstallmentCalculator.calculate_remaining_amount(self, self.total_paid)
    
    @property
    def remaining_months(self):
        return InstallmentCalculator.calculate_remaining_months(self, self.remaining_amount)
    
    @property
    def last_payment_date(self):
        return InstallmentCalculator.calculate_last_payment_date(self, self.remaining_months)
        
    @property
    def progress_percentage(self):
        return InstallmentCalculator.calculate_progress_percentage(self.total_paid, self.total_price)

    @property
    def is_paid(self):
        return InstallmentCalculator.calculate_is_paid(self.total_paid, self.total_price)
    
    
