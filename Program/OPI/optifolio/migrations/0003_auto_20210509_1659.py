# Generated by Django 3.2.1 on 2021-05-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optifolio', '0002_auto_20210509_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]