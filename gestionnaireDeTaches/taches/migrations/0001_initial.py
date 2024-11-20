# Generated by Django 5.0.7 on 2024-11-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('termine', models.BooleanField(default=False)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]