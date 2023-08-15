from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MainData, MusicPlayer, Gallery, VideoPlayer, ContactUs
from .forms import ContactForm
from django.views.generic import CreateView, ListView
from django.contrib import messages
from account.models import AccountHits, IPAddress
from datetime import date
from django.http import HttpResponse
# Create your views here.


class HomeInformation(ListView):
    model = AccountHits
    template_name = 'index.html'


    def get_object(self, queryset=None):
        today = date.today()
        daily_view, created = AccountHits.objects.get_or_create(date=today)
        
        user_ip = self.request.META.get('REMOTE_ADDR')
        
        if not daily_view.hits.filter(ip_address=user_ip).exists():
            daily_view.view_count += 1
            unique_ip, created = IPAddress.objects.get_or_create(ip_address=user_ip)
            daily_view.hits.add(unique_ip)
            daily_view.save()
        return daily_view
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = MainData.objects.first()
        context['music'] = MusicPlayer.objects.published().order_by("-publish")
        context['video'] = VideoPlayer.objects.published().order_by("-publish")
        context['gallery'] = Gallery.objects.all().order_by("-created")
        context['form'] = ContactForm()
        today = date.today()
        daily_view, created = AccountHits.objects.get_or_create(date=today)
        
        user_ip = self.request.META.get('REMOTE_ADDR')
        
        if not daily_view.hits.filter(ip_address=user_ip).exists():
            daily_view.view_count += 1
            unique_ip, created = IPAddress.objects.get_or_create(ip_address=user_ip)
            daily_view.hits.add(unique_ip)
            daily_view.save()
        context['daily_view'] = daily_view
        return context


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, 'Contact request submitted successfully.')

            return HttpResponseRedirect(reverse('homepage:information'))
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)


        return self.get(request, *args, **kwargs)