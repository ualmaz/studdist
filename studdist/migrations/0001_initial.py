# Generated by Django 3.1.2 on 2020-10-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('country', models.CharField(max_length=255, verbose_name='Country name')),
                ('city', models.CharField(max_length=255, verbose_name='City name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
