# Generated by Django 4.1.10 on 2023-07-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio45_code', '0011_alter_seminarinformation_cost_of_seminar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminarinformation',
            name='title',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]