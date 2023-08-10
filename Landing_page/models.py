from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class ProjectManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class MainData(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    header_logo = models.ImageField(upload_to="logo")
    footer_logo = models.ImageField(upload_to="logo")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('account:info', args=[self.pk] )


class SocialLinks(models.Model):
    label = models.CharField(max_length=120)
    icon = models.CharField(max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(MainData, null=True, on_delete=models.SET_NULL, related_name='socials')

    def __str__(self):
        return self.label


class MusicPlayer(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    title= models.CharField(max_length=150)
    album= models.CharField(max_length=150)
    image= models.ImageField(upload_to='cover', null=True)
    audio_file = models.FileField(blank=True,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    objects = ProjectManager()


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    data_file = models.ImageField(upload_to="gallery")
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class VideoPlayer(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    title= models.CharField(max_length=150)
    album= models.CharField(max_length=150)
    image= models.ImageField(upload_to='video-cover', null=True)
    data_file = models.FileField(blank=True,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    objects = ProjectManager()



class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.subject