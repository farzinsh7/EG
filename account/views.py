from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Landing_page.models import MainData, Gallery, MusicPlayer
from django.urls import reverse_lazy


@login_required
def account(request):
    return render(request, 'registration/account.html')


class Information(LoginRequiredMixin, UpdateView):
    template_name = 'registration/information.html'
    model = MainData
    fields = ['title', 'description', 'header_logo', 'footer_logo']


class GalleryList(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = 'registration/gallery_list.html'
    paginate_by = 2
    queryset = Gallery.objects.all().order_by("-created")

    
class GalleryCreate(LoginRequiredMixin, CreateView):
    model = Gallery
    template_name = 'registration/gallery_create.html'
    fields = ['title', 'data_file']


class GalleryDelete(LoginRequiredMixin, DeleteView):
    model = Gallery
    template_name = 'registration/gallery_form_delete.html'
    success_url = reverse_lazy('account:gallery')
    fields = ['title', 'data_file', 'created']


class SongsList(LoginRequiredMixin, ListView):
    model = MusicPlayer
    template_name = 'registration/songs_list.html'
    paginate_by = 2
    queryset = MusicPlayer.objects.all().order_by("-created")

    
class SongCreate(LoginRequiredMixin, CreateView):
    model = MusicPlayer
    template_name = 'registration/song_create.html'
    fields = ['title', 'album', 'image', 'audio_file', 'publish', 'status']


class SongUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'registration/song_create.html'
    model = MusicPlayer
    fields = ['title', 'album', 'image', 'audio_file', 'publish', 'status']


class SongDelete(LoginRequiredMixin, DeleteView):
    model = MusicPlayer
    template_name = 'registration/song_form_delete.html'
    success_url = reverse_lazy('account:songs')
    fields = ['title', 'album', 'image', 'audio_file', 'publish', 'status']