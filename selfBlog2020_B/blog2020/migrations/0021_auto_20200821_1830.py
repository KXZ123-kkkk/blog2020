# Generated by Django 3.0.7 on 2020-08-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2020', '0020_cartoon_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartoon',
            name='videoInfo',
        ),
        migrations.AddField(
            model_name='cartoon',
            name='videoInfo',
            field=models.ManyToManyField(to='blog2020.Video', verbose_name='视频URL'),
        ),
    ]
