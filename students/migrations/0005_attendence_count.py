# Generated by Django 5.0.6 on 2024-06-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_attendence_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
