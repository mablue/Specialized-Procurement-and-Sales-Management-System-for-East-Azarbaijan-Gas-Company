# Generated by Django 2.2.4 on 2019-08-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasfie', '0006_auto_20190818_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasfie',
            name='bank',
            field=models.CharField(default='ملت', max_length=500, verbose_name='نام بانک'),
        ),
    ]
