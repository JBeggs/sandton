# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 05:26
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20160910_0526'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery'),
        ),
        migrations.AlterField(
            model_name='colour',
            name='colour',
            field=colorfield.fields.ColorField(default='#000000', max_length=10),
        ),
    ]