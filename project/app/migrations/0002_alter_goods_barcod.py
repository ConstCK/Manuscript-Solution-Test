# Generated by Django 4.2.6 on 2023-10-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='BARCOD',
            field=models.CharField(max_length=256, null=True, verbose_name='Штрихкод'),
        ),
    ]
