# Generated by Django 4.0.4 on 2022-05-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='Duration',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
