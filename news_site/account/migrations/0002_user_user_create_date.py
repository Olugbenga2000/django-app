# Generated by Django 2.2.1 on 2019-11-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]