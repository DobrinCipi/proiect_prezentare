# Generated by Django 4.1.4 on 2023-04-19 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_digital', '0009_elevi_nume_parinte_alter_elevi_clasa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elevi',
            name='scoala',
        ),
    ]
