# Generated by Django 4.1.10 on 2023-07-26 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio45_code', '0007_schoolgym_entry_associate_schoolgym_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolgym',
            old_name='image',
            new_name='image_urls',
        ),
    ]