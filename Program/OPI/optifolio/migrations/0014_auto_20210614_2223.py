# Generated by Django 3.2.1 on 2021-06-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optifolio', '0013_visdata_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visdata',
            name='course',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=999, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='fare',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=999, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='shares_number',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=999, null=True),
        ),
    ]
