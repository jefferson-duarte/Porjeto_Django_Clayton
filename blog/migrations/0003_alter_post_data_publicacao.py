# Generated by Django 4.1 on 2022-08-31 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 23, 48, 48, 835860)),
        ),
    ]
