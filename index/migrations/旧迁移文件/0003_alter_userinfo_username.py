# Generated by Django 3.2.16 on 2023-01-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_userinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=24, verbose_name='用户注册'),
        ),
    ]
