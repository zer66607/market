# Generated by Django 2.0.2 on 2018-02-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerShop', '0005_auto_20180224_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
