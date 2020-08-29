# Generated by Django 3.0.7 on 2020-07-20 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20200719_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='written',
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cls',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.ClassList', verbose_name='问卷班级'),
        ),
    ]