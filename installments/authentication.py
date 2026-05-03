from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # 1. Look for the 'access_token' in the browser's cookies
        raw_token = request.COOKIES.get('access_token')
        
        if raw_token is None:
            return None

        # 2. If found, validate it using the standard JWT logic
        validated_token = self.get_validated_token(raw_token)
        
        # 3. Return the user and the token to Django
        return self.get_user(validated_token), validated_token