# your_app/middleware.py

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class BlockLoginIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated and trying to access login
        if request.user.is_authenticated and request.path == '/user_login/':
            return redirect('main2')    
        return self.get_response(request)