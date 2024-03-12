# Generated by Django 5.0.3 on 2024-03-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dept', models.CharField(max_length=255)),
                ('isguide', models.IntegerField(default=0)),
                ('ischair', models.IntegerField(default=0)),
                ('iscommem', models.IntegerField(default=0)),
                ('isprojcoo', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=9, unique=True)),
                ('domain', models.CharField(max_length=255)),
            ],
        ),
    ]
