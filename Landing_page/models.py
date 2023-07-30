from django.db import models
from django.utils import timezone


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
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    objects = ProjectManager()


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    main_img = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.title