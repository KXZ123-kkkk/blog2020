# Generated by Django 3.0.7 on 2020-08-09 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2020', '0005_music_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavemessage',
            name='replyName',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='回复者'),
        ),
    ]