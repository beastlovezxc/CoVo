# Generated by Django 3.0.5 on 2020-04-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helper_number', models.IntegerField(default=0)),
                ('activity_number', models.IntegerField(default=0)),
                ('helper_name', models.CharField(max_length=20)),
                ('activity_name', models.CharField(max_length=20)),
                ('feedback', models.TextField()),
                ('feedback_time', models.DateField()),
            ],
        ),
    ]
