# Generated by Django 3.0.7 on 2020-07-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200712_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d/', verbose_name='图片'),
        ),
    ]