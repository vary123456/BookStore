# Generated by Django 3.2.16 on 2023-01-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20230108_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub',
            name='public_id',
            field=models.BigIntegerField(unique=True, verbose_name='出版社主键'),
        ),
    ]
