# Generated by Django 3.2.7 on 2021-10-20 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optifolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='visdata',
            name='buy_sell',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='course',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=999, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='fare',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=999, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='shares_number',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=999, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='visdata',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='optifolio.customer'),
        ),
    ]
