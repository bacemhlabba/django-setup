# Generated by Django 4.2.1 on 2024-12-31 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_remove_company_job_titles_remove_company_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
