# Generated by Django 4.2.1 on 2024-12-31 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='job_titles',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='education',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='candidate',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='JobTitle',
        ),
    ]