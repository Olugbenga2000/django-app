# Generated by Django 2.2.1 on 2019-10-28 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupmember',
            unique_together=set(),
        ),
    ]
