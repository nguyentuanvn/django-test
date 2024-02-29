from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django_test.services.google_oauth import GoogleOauthService


class GoogleOauthRedirectAPI(View):
    def get(self, request, *args, **kwargs):
        google_oauth_service = GoogleOauthService()
        authorization_url = google_oauth_service.get_authorization_url()
        return redirect(authorization_url)

class GoogleOauthAPI(View):
    def get(self, request, *args, **kwargs):
        google_oauth_services = GoogleOauthService()
        code = request.GET.get("code")
        google_tokens = google_oauth_services.get_tokens(code=code)
        user_info = google_oauth_services.get_user_info(google_tokens=google_tokens)
        user_email = user_info["email"]
        if User.objects.filter(email=user_email).exists():
            user = User.objects.get(email=user_email)
        else:
            user = User.objects.create_user(username=user_email, email=user_email)
        login(request, user)
        return redirect("http://localhost:8000/")
