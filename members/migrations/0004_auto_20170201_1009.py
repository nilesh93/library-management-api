# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_membertypes_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
        migrations.RenameModel(
            old_name='MemberTypes',
            new_name='MemberType',
        ),
    ]
