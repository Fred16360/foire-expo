# Generated by Django 4.0.1 on 2022-02-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exposant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom_categorie',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='exposant',
            name='ville',
            field=models.CharField(max_length=50),
        ),
    ]
