# Generated by Django 4.1.3 on 2023-01-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('SLNo', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Desc', models.CharField(max_length=500)),
            ],
        ),
    ]
