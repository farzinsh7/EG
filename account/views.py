from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Landing_page.models import MainData, Gallery, MusicPlayer, VideoPlayer, ContactUs
from django.urls import reverse_lazy
from .forms import ContactForms


class Account(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = 'registration/account.html'


class Information(LoginRequiredMixin, UpdateView):
    template_name = 'registration/information.html'
    model = MainData
    fields = ['title', 'description', 'header_logo', 'footer_logo']


# Gallery admin Panel -------------

class GalleryList(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = 'registration/gallery_list.html'
    paginate_by = 10
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


# Songs admin Panel -------------

class SongsList(LoginRequiredMixin, ListView):
    model = MusicPlayer
    template_name = 'registration/songs_list.html'
    paginate_by = 10
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


# Videos admin Panel -------------

class VideosList(LoginRequiredMixin, ListView):
    model = VideoPlayer
    template_name = 'registration/videos_list.html'
    paginate_by = 10
    queryset = VideoPlayer.objects.all().order_by("-created")

    
class VideoCreate(LoginRequiredMixin, CreateView):
    model = VideoPlayer
    template_name = 'registration/video_create.html'
    fields = ['title', 'album', 'image', 'data_file', 'publish', 'status']


class VideoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'registration/video_create.html'
    model = VideoPlayer
    fields = ['title', 'album', 'image', 'data_file', 'publish', 'status']


class VideoDelete(LoginRequiredMixin, DeleteView):
    model = VideoPlayer
    template_name = 'registration/video_form_delete.html'
    success_url = reverse_lazy('account:videos')
    fields = ['title', 'album', 'image', 'data_file', 'publish', 'status']


# Contact admin Panel -------------
class MessageList(LoginRequiredMixin, ListView):
    model = ContactUs
    template_name = 'registration/message_list.html'
    paginate_by = 10
    queryset = ContactUs.objects.all().order_by("-created")
    

class MessageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'registration/message_update.html'
    model = ContactUs
    form_class = ContactForms


class MessageDelete(LoginRequiredMixin, DeleteView):
    model = ContactUs
    template_name = 'registration/message_delete.html'
    success_url = reverse_lazy('account:message')
    fields = ['name', 'email', 'subject', 'message', 'status']

