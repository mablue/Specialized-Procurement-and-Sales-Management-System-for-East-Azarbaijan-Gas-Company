# Generated by Django 2.2.4 on 2019-08-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taghaza', '0014_auto_20190811_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='taghaza',
            name='baravord',
            field=models.IntegerField(null=True, verbose_name='مبلغ براورد اولیه'),
        ),
        migrations.AlterField(
            model_name='taghaza',
            name='shomare',
            field=models.CharField(default=1234213, max_length=10, unique=True, verbose_name='شماره تقاضا'),
            preserve_default=False,
        ),
    ]
