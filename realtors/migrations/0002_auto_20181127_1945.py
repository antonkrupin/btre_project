# Generated by Django 2.0.9 on 2018-11-27 19:45

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='realtor',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
