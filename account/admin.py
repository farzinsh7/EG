from django.contrib import admin
from . import models
from .models import User, IPAddress, AccountHits

# Register your models here.
@admin.register(models.User)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'username']


admin.site.register(IPAddress)
admin.site.register(AccountHits)