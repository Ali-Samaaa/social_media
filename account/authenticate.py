from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user:
                login(request, user)
                messages.success(request, 'you login successfully', 'success')
                return redirect('home:home')
            else:
                return None

