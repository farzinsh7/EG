from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import IPAddress, User, AccountHits
from Landing_page.models import MainData, Gallery, MusicPlayer, VideoPlayer, ContactUs
from django.urls import reverse_lazy
from .forms import ContactForms, ProfileForms
from datetime import date
from datetime import datetime, timedelta


class Account(LoginRequiredMixin, ListView):
    model = AccountHits
    template_name = 'registration/account.html'
    # queryset = MusicPlayer.objects.all().count    

    def get_object(self):
        account_hits = AccountHits.objects.all()
        ip_address = self.request.user.ip_address
        if ip_address not in account_hits.hints.all():
            account_hits.hits.add(ip_address)
        return account_hits

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music'] = MusicPlayer.objects.all().count
        context['video'] = VideoPlayer.objects.all().count
        context['message'] = ContactUs.objects.all().count
        context['account'] = IPAddress.objects.all().count
        today = datetime.now().date()
        seven_days_ago = today - timedelta(days=7)
        context['view_data'] = AccountHits.objects.filter(date__range=[seven_days_ago, today])
        return context



class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')
    form_class = ProfileForms

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")


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

