# Generated by Django 4.1.10 on 2023-07-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio45_code', '0004_user_dob_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolgym',
            name='state',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='days_of_operation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='hours_of_operation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='introduction',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='owner_email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='owner_first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='owner_last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='owner_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='owner_social_media_links',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='price_max_ranges',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='price_min_ranges',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='special_instructions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolgym',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]