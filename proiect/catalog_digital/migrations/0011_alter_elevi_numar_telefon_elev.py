# Generated by Django 4.1.4 on 2023-04-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_digital', '0010_remove_elevi_scoala'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevi',
            name='numar_telefon_elev',
            field=models.CharField(max_length=10),
        ),
    ]
