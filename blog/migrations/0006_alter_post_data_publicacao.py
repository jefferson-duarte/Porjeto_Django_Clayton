# Generated by Django 4.1 on 2022-09-21 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_imagem_capa_post_resumo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 9, 55, 42, 902068, tzinfo=datetime.timezone.utc)),
        ),
    ]
