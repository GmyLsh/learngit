# Generated by Django 2.1.2 on 2018-11-06 09:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='promession_users',
            field=models.ManyToManyField(null=True, related_name='promession_users', to=settings.AUTH_USER_MODEL, verbose_name='授权用户'),
        ),
    ]
