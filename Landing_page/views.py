from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MainData, MusicPlayer, Gallery, VideoPlayer, ContactUs
from .forms import ContactForm
from django.views.generic import CreateView, ListView
from django.contrib import messages

# Create your views here.


class HomeInformation(ListView):
    model = MainData
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = MainData.objects.first()
        context['music'] = MusicPlayer.objects.published().order_by("-publish")
        context['video'] = VideoPlayer.objects.published().order_by("-publish")
        context['gallery'] = Gallery.objects.all().order_by("-created")
        context['form'] = ContactForm()
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