from rest_framework_simplejwt.views import TokenObtainPairView
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
