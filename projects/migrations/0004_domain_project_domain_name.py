# Generated by Django 5.0.3 on 2024-03-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_phase_remove_project_eval1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='domain_name',
            field=models.ManyToManyField(blank=True, related_name='Domain', to='projects.domain'),
        ),
    ]