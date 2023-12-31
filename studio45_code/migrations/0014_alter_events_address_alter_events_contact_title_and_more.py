# Generated by Django 4.1.10 on 2023-07-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio45_code', '0013_schoolgym_status_seminarinformation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='address',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='contact_title',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='owner_email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seminarinformation',
            name='address',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seminarinformation',
            name='organizer_email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seminarinformation',
            name='title',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
