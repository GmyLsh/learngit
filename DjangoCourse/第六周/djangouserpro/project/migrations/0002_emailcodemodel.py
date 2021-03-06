# Generated by Django 2.1.2 on 2018-11-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCodeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('send_type', models.CharField(choices=[('register', '激活'), ('forget', '忘记密码')], max_length=30)),
            ],
        ),
    ]
