# Generated by Django 4.2.3 on 2023-08-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounthits',
            name='date',
            field=models.DateField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='accounthits',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
