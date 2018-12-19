# Generated by Django 2.1.2 on 2018-11-17 20:51

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=20, null=True, verbose_name='用户昵称')),
                ('mobile', models.CharField(max_length=20, null=True, verbose_name='电话')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='住址')),
                ('head_img', models.ImageField(null=True, upload_to='img/%Y/%m', verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AD_title', models.CharField(max_length=20, verbose_name='广告标题')),
                ('AD_address', models.CharField(max_length=50, verbose_name='广告地址')),
                ('AD_img_url', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': '广告',
                'verbose_name_plural': '广告',
                'db_table': 'AD',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_publish_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='创建时间')),
                ('a_title', models.CharField(max_length=20, verbose_name='文章标题')),
                ('a_content', models.CharField(max_length=100, verbose_name='文章内容')),
                ('a_label', models.CharField(max_length=20, verbose_name='标签')),
                ('a_look', models.IntegerField(null=True, verbose_name='浏览量')),
                ('a_comment', models.IntegerField(null=True, verbose_name='评论数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_label', models.CharField(max_length=20, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'label',
            },
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_sort_name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('a_sort', models.IntegerField(null=True, verbose_name='排序')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'sort',
            },
        ),
    ]
