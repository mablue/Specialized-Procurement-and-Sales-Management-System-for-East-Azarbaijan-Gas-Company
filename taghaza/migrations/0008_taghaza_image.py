# Generated by Django 2.2.4 on 2019-08-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taghaza', '0007_remove_taghaza_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='taghaza',
            name='image',
            field=models.ImageField(default='TaghazaPictures/def.jpg', height_field=500, upload_to='TaghazaPictures/', verbose_name='تصویر فرم تقاضای کالا (MT26)', width_field=500),
        ),
    ]
