# Generated by Django 5.2 on 2025-05-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('pernom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('objet', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
