# Generated by Django 3.2.16 on 2023-01-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_userinfo_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fd01', models.CharField(max_length=10, verbose_name='字段1')),
                ('fd02', models.CharField(max_length=40, verbose_name='字段2')),
            ],
        ),
    ]
