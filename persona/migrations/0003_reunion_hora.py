# Generated by Django 4.0.5 on 2022-06-22 01:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_hobby_reunion_person_hobbies'),
    ]

    operations = [
        migrations.AddField(
            model_name='reunion',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
