# Generated by Django 2.2.4 on 2019-08-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pardaxt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pardaxt',
            name='hesab',
            field=models.CharField(max_length=300, verbose_name='شماره حساب'),
        ),
    ]
