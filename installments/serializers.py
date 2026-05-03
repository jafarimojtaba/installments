from rest_framework import serializers
from .models import Installment

class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        # These are the fields that will be visible in your JSON API
        fields = [
            'id',
            'name',
            'total_price',
            'monthly_amount',
            'first_payment_date',
            'last_payment_date',
            'total_paid',
            'remaining_months',
            'remaining_amount',
            'progress_percentage',
            'is_paid',
            'purchase_date',
            'pay_day',
        ]
        # We can also add "read-only" calculated fields here later!
        read_only_fields = ['total_paid', 'remaining_amount', 'progress_percentage', 'is_paid', 'remaining_months']
