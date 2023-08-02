from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    

@login_required
def account(request):
    return render(request, 'registration/account.html')