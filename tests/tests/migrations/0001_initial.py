# Generated by Django 2.2 on 2020-07-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RandomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField(unique=True)),
                ('value', models.IntegerField(default=0)),
                ('data', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
