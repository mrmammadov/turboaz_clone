# Generated by Django 3.2 on 2021-05-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=50)),
            ],
        ),
    ]
