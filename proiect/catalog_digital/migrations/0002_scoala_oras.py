# Generated by Django 4.1.4 on 2023-03-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_digital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoala',
            name='oras',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
