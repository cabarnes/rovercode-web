# Generated by Django 2.2.2 on 2019-06-24 02:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mission_control', '0013_auto_20190417_1558'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='blockdiagram',
            unique_together={('user', 'name')},
        ),
    ]
