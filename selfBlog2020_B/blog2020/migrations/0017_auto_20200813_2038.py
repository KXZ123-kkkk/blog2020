# Generated by Django 3.0.7 on 2020-08-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2020', '0016_replymessage_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemessage',
            name='owner',
            field=models.IntegerField(choices=[(1, 'Me'), (2, 'Blog')], default=1, max_length=16, verbose_name='属于'),
        ),
        migrations.AlterField(
            model_name='replymessage',
            name='owner',
            field=models.IntegerField(choices=[(1, 'Me'), (2, 'Blog')], default=1, max_length=16, verbose_name='属于'),
        ),
    ]