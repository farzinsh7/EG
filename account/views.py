from django.shortcuts import render
from django.contrib.auth.decorators import login_required
    

@login_required
def account(request):
    return render(request, 'registration/account.html')