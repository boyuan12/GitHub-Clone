# Generated by Django 3.1.3 on 2020-11-27 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201117_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyPICredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('token', models.CharField(max_length=1000)),
            ],
        ),
    ]