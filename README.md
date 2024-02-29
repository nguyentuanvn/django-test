# django-test
There are two servers: 
- Django's HTTP server
- gRPC API server

## To run in development:
  python manage.py runserver
  python manage.py grpcserver

## Run in docker:
  docker-compose up -d
Both servers are up and running

## Google Oauth:
Need to provide Google API client_id and secret in environment variable in order to use Google Oauth

  GOOGLE_OAUTH_CLIENT_ID=""
  
  GOOGLE_OAUTH_CLIENT_SECRET=""
