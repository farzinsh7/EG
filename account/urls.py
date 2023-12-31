from django.contrib.auth import views
from django.urls import path
from .views import Account, Information, GalleryList, GalleryDelete, GalleryCreate, SongsList, SongCreate,SongDelete, SongUpdate, VideoCreate, VideoDelete, VideosList, VideoUpdate, MessageList, MessageUpdate, MessageDelete, ProfileView, PasswordChange

app_name = "account"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password_change/", PasswordChange.as_view(), name="password_change"),
    path("password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done",),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done",),
    # path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm",),
    # path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
]

urlpatterns += [
    path("", Account.as_view(), name="dashboard"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("info/<int:pk>", Information.as_view(), name="info"),
    path("gallery/", GalleryList.as_view(), name="gallery"),
    path("gallery/create/", GalleryCreate.as_view(), name="gallery_create"),
    path("gallery/delete/<int:pk>", GalleryDelete.as_view(), name="gallery_delete"),
    path("song/", SongsList.as_view(), name="songs"),
    path("song/create/", SongCreate.as_view(), name="song_create"),
    path("song/update/<int:pk>", SongUpdate.as_view(), name="song_update"),
    path("song/delete/<int:pk>", SongDelete.as_view(), name="song_delete"),
    path("video/", VideosList.as_view(), name="videos"),
    path("video/create/", VideoCreate.as_view(), name="video_create"),
    path("video/update/<int:pk>", VideoUpdate.as_view(), name="video_update"),
    path("video/delete/<int:pk>", VideoDelete.as_view(), name="video_delete"),
    path("message/", MessageList.as_view(), name="message"),
    path("message/update/<int:pk>", MessageUpdate.as_view(), name="message_update"),
    path("message/delete/<int:pk>", MessageDelete.as_view(), name="message_delete"),

]
