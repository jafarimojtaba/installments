from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Installment
from .serializers import InstallmentSerializer


class InstallmentViewSet(viewsets.ModelViewSet):
    serializer_class = InstallmentSerializer
    # Only authenticated users can access this view
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Admins can see all installments, regular users only see their own
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Installment.objects.all()
        return Installment.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    