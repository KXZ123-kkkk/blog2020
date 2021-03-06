# Generated by Django 3.0.7 on 2020-07-08 12:19

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('character', models.IntegerField(choices=[(1, '学生'), (2, '工作人员')], default=1, verbose_name='角色')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='学生账号')),
                ('password', models.CharField(max_length=628, verbose_name='学生密码')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('className', models.CharField(max_length=32, verbose_name='班级名')),
            ],
            options={
                'verbose_name': '班级表',
                'verbose_name_plural': '班级表',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('title', models.CharField(max_length=32, verbose_name='问卷名')),
                ('cls', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='survey.ClassList', verbose_name='问卷班级')),
                ('create_user', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建问卷的用户')),
            ],
            options={
                'verbose_name': '问卷表',
                'verbose_name_plural': '问卷表',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('question', models.CharField(max_length=32, verbose_name='问题题目')),
                ('question_type', models.IntegerField(choices=[(1, '打分'), (2, '单选'), (3, '评价')], default=2, verbose_name='问题类型')),
                ('questionnaire', models.ManyToManyField(blank=True, null=True, to='survey.Questionnaire', verbose_name='所属问卷')),
            ],
            options={
                'verbose_name': '问卷问题表',
                'verbose_name_plural': '问卷问题表',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('name', models.CharField(max_length=32, verbose_name='选项名')),
                ('score', models.IntegerField(verbose_name='选项对应的分值')),
                ('question', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='survey.Questions', verbose_name='所属问题')),
            ],
            options={
                'verbose_name': '问卷单选题的选项表',
                'verbose_name_plural': '问卷单选题的选项表',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('val', models.IntegerField(blank=True, null=True, verbose_name='数字答案')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='文本答案')),
                ('option', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Option', verbose_name='单选选项')),
                ('question', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='survey.Questions', verbose_name='所属问题')),
                ('student', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属学生')),
            ],
            options={
                'verbose_name': '问卷回答表',
                'verbose_name_plural': '问卷回答表',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cls',
            field=models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.ClassList', verbose_name='所属班级'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
