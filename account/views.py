from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Landing_page.models import MainData
    

@login_required
def account(request):
    return render(request, 'registration/account.html')


class Information(UpdateView):
    template_name = 'registration/information.html'
    model = MainData
    fields = ['title', 'description', 'header_logo', 'footer_logo']