# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 18:45
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('colour', colorfield.fields.ColorField(default='#FF0000', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('blurb', models.TextField()),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('unit_of_weight', models.CharField(blank=True, choices=[[b'gram', b'gram'], [b'kilogram', b'kilogram'], [b'ton', b'ton']], max_length=10, null=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('colours', models.ManyToManyField(to='catalog.Colour')),
                ('fabric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Fabric')),
            ],
        ),
    ]