from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect


def homepage(request):
    return render(request, 'homepage.html', { "authenticated": request.user.is_authenticated })

def logout_view(request):
    logout(request)
    return redirect("http://localhost:8000")
