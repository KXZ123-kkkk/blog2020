# Generated by Django 3.0.7 on 2020-08-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2020', '0015_auto_20200813_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='replymessage',
            name='owner',
            field=models.CharField(choices=[(1, 'Me'), (2, 'Blog')], default=1, max_length=16, verbose_name='属于'),
        ),
    ]
