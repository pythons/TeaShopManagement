# Generated by Django 2.1.4 on 2018-12-27 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamanagement', '0002_auto_20181227_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity_info',
            name='commodity_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='purchase_info',
            name='total_price',
            field=models.FloatField(),
        ),
    ]