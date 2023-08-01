from django.contrib import admin
from .models import MainData, MusicPlayer, Gallery, SocialLinks, VideoPlayer, ContactUs


class SocialLinksAdmin(admin.TabularInline):
    model = SocialLinks
    extra = 1
    max_num = 10


@admin.register(MainData)
class MainDataAdmin(admin.ModelAdmin):
    inlines = [SocialLinksAdmin]


admin.site.register(Gallery)
admin.site.register(MusicPlayer)
admin.site.register(VideoPlayer)
admin.site.register(ContactUs)
