# Generated by Django 4.1.7 on 2023-06-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio45_code', '0003_alter_events_website_alter_schoolgym_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
