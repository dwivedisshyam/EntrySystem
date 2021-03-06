# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-07 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0005_auto_20181106_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goingTo', models.CharField(max_length=200)),
                ('purpose', models.CharField(max_length=200)),
                ('visitDate', models.DateTimeField(auto_now_add=True)),
                ('regNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.Student')),
            ],
        ),
    ]
