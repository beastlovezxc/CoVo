# Generated by Django 3.0.5 on 2020-04-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('account', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
