# Generated by Django 4.2.3 on 2023-08-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicplayer',
            name='arrngement',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='musicplayer',
            name='cover_art',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='musicplayer',
            name='songwriter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='videoplayer',
            name='cover_art',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='videoplayer',
            name='director',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='musicplayer',
            name='album',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='musicplayer',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='videoplayer',
            name='album',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='videoplayer',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]