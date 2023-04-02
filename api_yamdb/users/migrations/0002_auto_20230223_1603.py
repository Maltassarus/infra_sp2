# Generated by Django 3.2 on 2023-02-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', max_length=15),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_username_email'),
        ),
    ]