# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('contract_no', models.CharField(verbose_name='大ID', max_length=50)),
                ('image_url', models.CharField(verbose_name='图片URL', max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_date', models.DateTimeField(verbose_name='更新时间', null=True, auto_now=True)),
            ],
        ),
    ]
