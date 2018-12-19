# Generated by Django 2.1.2 on 2018-10-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default=None, max_length=20)),
                ('user_height', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
