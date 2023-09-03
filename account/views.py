from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import IPAddress, User, AccountHits
from Landing_page.models import MainData, Gallery, MusicPlayer, VideoPlayer, ContactUs, SocialLinks
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
        context['view_data'] = list(reversed(AccountHits.objects.filter(date__range=[seven_days_ago, today]).order_by('-date')[:7]))
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
    success_url = reverse_lazy('account:info', kwargs={'pk': 1})
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        main_data = self.get_object()

        # Create a formset for SocialLinks
        SocialLinksFormSet = inlineformset_factory(MainData, SocialLinks, fields=['label', 'link'], extra=0, can_delete=False)

        # Check if there is POST data (form submission) and update the formset accordingly
        if self.request.method == 'POST':
            social_links_formset = SocialLinksFormSet(self.request.POST, instance=main_data)
        else:
            social_links_formset = SocialLinksFormSet(instance=main_data)

        context['social_links_formset'] = social_links_formset

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        social_links_formset = context['social_links_formset']

        if form.is_valid() and social_links_formset.is_valid():
            # Save the changes to the MainData form
            main_data = form.save(commit=False)
            main_data.save()

            # Save the changes to the SocialLinks forms within the formset
            for social_links_form in social_links_formset:
                if social_links_form.cleaned_data:
                    social_links = social_links_form.save(commit=False)
                    social_links.main_data = main_data  # Set the relationship to the MainData instance
                    social_links.save()

            return redirect(self.success_url)

    # If the form or formset is not valid, re-render the form with errors
        return self.render_to_response(self.get_context_data(form=form, social_links_formset=social_links_formset))



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
    fields = ['title', 'album', 'songwriter', 'cover_art', 'arrngement', 'image', 'audio_file', 'publish', 'status']


class SongUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'registration/song_create.html'
    model = MusicPlayer
    fields = ['title', 'album', 'songwriter', 'cover_art', 'arrngement', 'image', 'audio_file', 'publish', 'status']


class SongDelete(LoginRequiredMixin, DeleteView):
    model = MusicPlayer
    template_name = 'registration/song_form_delete.html'
    success_url = reverse_lazy('account:songs')
    fields = ['title', 'album', 'songwriter', 'cover_art', 'arrngement', 'image', 'audio_file', 'publish', 'status']


# Videos admin Panel -------------

class VideosList(LoginRequiredMixin, ListView):
    model = VideoPlayer
    template_name = 'registration/videos_list.html'
    paginate_by = 10
    queryset = VideoPlayer.objects.all().order_by("-created")

    
class VideoCreate(LoginRequiredMixin, CreateView):
    model = VideoPlayer
    template_name = 'registration/video_create.html'
    fields = ['title', 'album', 'director', 'cover_art', 'image', 'data_file', 'publish', 'status']


class VideoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'registration/video_create.html'
    model = VideoPlayer
    fields = ['title', 'album', 'director', 'cover_art', 'image', 'data_file', 'publish', 'status']


class VideoDelete(LoginRequiredMixin, DeleteView):
    model = VideoPlayer
    template_name = 'registration/video_form_delete.html'
    success_url = reverse_lazy('account:videos')
    fields = ['title', 'album', 'director', 'cover_art', 'image', 'data_file', 'publish', 'status']


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

