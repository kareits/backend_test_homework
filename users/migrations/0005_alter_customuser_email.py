# Generated by Django 3.2.16 on 2023-10-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Пользователь с таким email уже зарегистрирован'}, max_length=254, unique=True, verbose_name='email'),
        ),
    ]
