# Generated by Django 5.0.6 on 2024-06-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_rename_attend_attendence_register4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]
