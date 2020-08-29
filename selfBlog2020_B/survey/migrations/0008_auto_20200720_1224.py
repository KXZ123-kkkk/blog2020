# Generated by Django 3.0.7 on 2020-07-20 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20200720_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='create_user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建问卷的用户'),
        ),
    ]
