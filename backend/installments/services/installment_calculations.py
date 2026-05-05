from datetime import date
from calendar import monthrange


class InstallmentCalculator:
    """Service class for installment-related calculations"""
    
    @staticmethod
    def calculate_total_paid(installment):
        """Calculate total amount paid to date"""
        today = date.today()
        first_due = installment.first_payment_date
        
        if first_due > today:
            return installment.monthly_amount * 0

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
            day = min(installment.pay_day, last_day)
            due = date(year, month, day)

        return installment.monthly_amount * months_count
    
    @staticmethod
    def calculate_remaining_amount(installment, total_paid):
        """Calculate remaining balance"""
        return installment.total_price - total_paid
    
    @staticmethod
    def calculate_remaining_months(installment, remaining_amount):
        """Calculate months remaining to pay"""
        return round((installment.total_price - remaining_amount) / installment.monthly_amount)
    
    @staticmethod
    def calculate_last_payment_date(installment, remaining_months):
        """Calculate the final payment date"""
        year = installment.first_payment_date.year
        month = installment.first_payment_date.month + remaining_months
        
        # Adjust year if month exceeds 12
        while month > 12:
            month -= 12
            year += 1
        
        # Clamp day to last day of target month
        last_day = monthrange(year, month)[1]
        day = min(installment.first_payment_date.day, last_day)
        
        return date(year, month, day)
    
    @staticmethod
    def calculate_progress_percentage(total_paid, total_price):
        """Calculate payment progress as percentage"""
        return round((total_paid / total_price) * 100)
    
    @staticmethod
    def calculate_is_paid(total_paid, total_price):
        """Check if payment is complete"""
        return total_paid >= total_price
