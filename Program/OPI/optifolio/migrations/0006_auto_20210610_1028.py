# Generated by Django 3.2.1 on 2021-06-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optifolio', '0005_vistemp'),
    ]

    operations = [
        migrations.AddField(
            model_name='vistemp',
            name='fare',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=999),
        ),
        migrations.AlterField(
            model_name='vistemp',
            name='buy_sell',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='vistemp',
            name='course',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=999),
        ),
        migrations.AlterField(
            model_name='vistemp',
            name='shares_number',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=999),
        ),
    ]