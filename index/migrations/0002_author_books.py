# Generated by Django 3.2.16 on 2023-01-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='index.Book'),
        ),
    ]