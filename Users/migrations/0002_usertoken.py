# Generated by Django 3.0.5 on 2020-05-24 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=60)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.Users')),
            ],
        ),
    ]