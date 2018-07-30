# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-13 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180413_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nome')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='Assunto')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Email')),
                ('message', models.TextField(default='', verbose_name='Mensagem')),
            ],
        ),
    ]