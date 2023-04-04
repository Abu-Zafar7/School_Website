# Generated by Django 4.1.7 on 2023-04-03 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+999999999'. Up to 12 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
