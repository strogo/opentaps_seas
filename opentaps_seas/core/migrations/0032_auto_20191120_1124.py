# Generated by Django 2.1.11 on 2019-11-20 19:24

import cratedb.fields.array
import cratedb.fields.hstore
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20191120_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='meta_data',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
    ]
