# Generated by Django 3.2.16 on 2023-01-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='用户注册')),
                ('password', models.CharField(max_length=100, verbose_name='用户密码')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
