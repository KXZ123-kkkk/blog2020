# Generated by Django 3.0.7 on 2020-07-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20200713_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(default='img/default.jpg', upload_to='img', verbose_name='图片'),
        ),
    ]