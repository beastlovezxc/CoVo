# Generated by Django 3.0.5 on 2020-04-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('manager', models.BooleanField()),
            ],
        ),
    ]
