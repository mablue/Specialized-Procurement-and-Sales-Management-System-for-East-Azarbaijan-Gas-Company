# Generated by Django 2.2.4 on 2019-08-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aghlam', '0012_remove_aghlam_factor'),
        ('factor', '0005_remove_factor_aghlam'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='aghlam',
            field=models.ManyToManyField(to='aghlam.Aghlam'),
        ),
    ]
