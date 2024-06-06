# Generated by Django 5.0.6 on 2024-06-06 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_register_confirm_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('register2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.register')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('register1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.register')),
            ],
        ),
        migrations.CreateModel(
            name='Student_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.register')),
            ],
        ),
    ]
