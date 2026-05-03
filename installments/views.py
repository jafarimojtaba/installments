from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Installment
from .serializers import InstallmentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from rest_framework.response import Response

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            # Attach the access token as a cookie
            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,   # Prevents JS access 🛡️
                secure=False,    # Set to True in production (HTTPS)
                samesite='Lax',  # CSRF protection
            )
            
            # You can do the same for the refresh token
        return response

class InstallmentViewSet(viewsets.ModelViewSet):
    serializer_class = InstallmentSerializer
    # Only authenticated users can access this view
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Only show installments for the current user
        return Installment.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    