# Generated by Django 3.0.7 on 2020-07-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200712_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='D:/media/img/', verbose_name='图片'),
        ),
    ]