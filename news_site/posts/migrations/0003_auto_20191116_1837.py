# Generated by Django 2.2.1 on 2019-11-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191028_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text_html',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Title', max_length=50),
            preserve_default=False,
        ),
    ]
