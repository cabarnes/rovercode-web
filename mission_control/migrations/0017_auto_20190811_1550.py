# Generated by Django 2.2.3 on 2019-08-11 15:50

import django.contrib.postgres.fields.citext
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission_control', '0016_auto_20190801_0117'),
    ]

    operations = [
        CITextExtension(),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.postgres.fields.citext.CICharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='blockdiagram',
            name='admin_tags',
            field=models.ManyToManyField(blank=True, related_name='admin_block_diagrams', to='mission_control.Tag'),
        ),
        migrations.AddField(
            model_name='blockdiagram',
            name='owner_tags',
            field=models.ManyToManyField(blank=True, related_name='owner_block_diagrams', to='mission_control.Tag'),
        ),
    ]
