from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Landing_page.models import MainData, Gallery
from django.urls import reverse_lazy


@login_required
def account(request):
    return render(request, 'registration/account.html')


class Information(UpdateView):
    template_name = 'registration/information.html'
    model = MainData
    fields = ['title', 'description', 'header_logo', 'footer_logo']


class GalleryList(ListView):
    model = Gallery
    template_name = 'registration/gallery_list.html'
    paginate_by = 10
    queryset = Gallery.objects.all().order_by("-created")

    
class GalleryCreate(CreateView):
    model = Gallery
    template_name = 'registration/gallery_create.html'
    fields = ['title', 'data_file']


class GalleryDelete(DeleteView):
    model = Gallery
    template_name = 'registration/gallery_form_delete.html'
    success_url = reverse_lazy('account:gallery')
    fields = ['title', 'data_file', 'created']


