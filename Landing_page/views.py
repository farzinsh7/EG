from django.shortcuts import render
from .models import MainData, MusicPlayer, Gallery
from django.views.generic import CreateView, ListView

# Create your views here.


class HomeInformation(ListView):
    model = MainData
    # form_class = ContactFormClass
    # success_url = reverse_lazy('homepage:information')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = MainData.objects.first()
        context['music'] = MusicPlayer.objects.all()
        context['gallery'] = Gallery.objects.all()
        return context