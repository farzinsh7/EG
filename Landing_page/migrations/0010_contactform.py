# Generated by Django 4.2.3 on 2023-08-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing_page', '0009_delete_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]