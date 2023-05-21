# Generated by Django 4.0.4 on 2022-05-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255, unique=True)),
                ('Address', models.CharField(max_length=255)),
                ('Number', models.IntegerField(unique=True)),
                ('Gender', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
                ('Availabe', models.IntegerField()),
                ('Actual', models.IntegerField()),
                ('Salary', models.IntegerField()),
                ('DOB', models.CharField(max_length=255)),
            ],
        ),
    ]
