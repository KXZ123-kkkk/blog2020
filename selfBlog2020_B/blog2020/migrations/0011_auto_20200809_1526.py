# Generated by Django 3.0.7 on 2020-08-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2020', '0010_auto_20200809_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemessage',
            name='nickName',
            field=models.CharField(max_length=64, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='replymessage',
            name='replyName',
            field=models.CharField(max_length=64, verbose_name='回复者'),
        ),
    ]