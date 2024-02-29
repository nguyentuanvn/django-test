import os
import requests
from urllib.parse import urlencode


class GoogleOauthService:

    GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_ACCESS_TOKEN_OBTAIN_URL = "https://oauth2.googleapis.com/token"
    GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

    SCOPES = [
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid",
    ]

    def __init__(self):
        self.redirect_uri = "http://localhost:8000/gauth/callback"
        self.client_id = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        self.client_secret = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")

    def get_authorization_url(self):
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": " ".join(self.SCOPES),
            "access_type": "offline",
            "include_granted_scopes": "true",
            "prompt": "select_account",
        }
        query_params = urlencode(params)
        authorization_url = f"{self.GOOGLE_AUTH_URL}?{query_params}"
        return authorization_url

    def get_tokens(self, *, code: str):
        data = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code",
        }
        response = requests.post(self.GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)
        if not response.ok:
            print("Failed to obtain access token from Google.")
        response = response.json()
        return response

    def get_user_info(self, *, google_tokens):
        access_token = google_tokens["access_token"]

        response = requests.get(
            self.GOOGLE_USER_INFO_URL,
            params={"access_token": access_token}
        )
        if not response.ok:
            print("Failed to obtain user info from Google.")
        response = response.json()
        return response
