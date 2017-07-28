from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'image/index.html')
