# Generated by Django 2.2.4 on 2019-08-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taghaza', '0008_taghaza_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taghaza',
            name='image',
            field=models.ImageField(upload_to='TaghazaPictures/', verbose_name='تصویر فرم تقاضای کالا (MT26)'),
        ),
    ]
