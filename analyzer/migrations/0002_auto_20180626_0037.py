# Generated by Django 2.0.6 on 2018-06-25 19:07
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        HStoreExtension(),
    ]
