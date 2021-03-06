# Generated by Django 3.0.7 on 2020-07-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='D:/media/img//%Y/%m/%d/', verbose_name='图片')),
            ],
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionnaire',
            field=models.ManyToManyField(blank=True, to='survey.Questionnaire', verbose_name='所属问卷'),
        ),
    ]
