# Generated by Django 4.2.7 on 2023-11-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomi', models.CharField(blank=True, max_length=1000, null=True)),
                ('Statiya', models.CharField(max_length=1000)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
