# Generated by Django 4.2.3 on 2023-07-26 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('main_img', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('header_logo', models.ImageField(upload_to='logo')),
                ('footer_logo', models.ImageField(upload_to='logo')),
            ],
        ),
        migrations.CreateModel(
            name='MusicPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('album', models.CharField(max_length=150)),
                ('image', models.ImageField(null=True, upload_to='cover')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='')),
                ('audio_link', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120)),
                ('icon', models.CharField(max_length=200)),
                ('main_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='socials', to='Landing_page.maindata')),
            ],
        ),
    ]