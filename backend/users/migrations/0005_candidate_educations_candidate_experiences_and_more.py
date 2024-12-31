# Generated by Django 4.2.1 on 2024-10-08 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_candidate_degree_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='educations',
            field=models.ManyToManyField(blank=True, related_name='candidates', to='users.education'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='experiences',
            field=models.ManyToManyField(blank=True, related_name='candidates', to='users.experience'),
        ),
        migrations.AlterField(
            model_name='education',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations_list', to='users.candidate'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences_list', to='users.candidate'),
        ),
    ]
