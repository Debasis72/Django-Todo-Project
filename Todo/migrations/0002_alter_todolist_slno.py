# Generated by Django 4.1.3 on 2023-01-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='SLNo',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
