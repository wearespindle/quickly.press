# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-17 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buttons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('emergency_button_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buttons.EmergencyButtonClient')),
            ],
        ),
    ]