# Generated by Django 2.1.2 on 2018-10-29 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=20)),
                ('a_pwd', models.CharField(max_length=10)),
                ('a_register_date', models.DateField(auto_now_add=True)),
                ('a_update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=20)),
                ('c_address', models.TextField()),
                ('c_phone', models.CharField(max_length=20)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orm.Account')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
