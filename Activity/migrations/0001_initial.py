# Generated by Django 3.0.5 on 2020-04-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_number', models.AutoField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=20)),
                ('introduction', models.TextField()),
                ('expired', models.BooleanField(default=False)),
                ('required_num', models.IntegerField(default=0)),
                ('participants', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=40)),
                ('activity_points', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]
