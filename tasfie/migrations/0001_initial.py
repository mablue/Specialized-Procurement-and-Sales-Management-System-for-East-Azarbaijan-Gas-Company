# Generated by Django 2.2.3 on 2019-07-19 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taghaza', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasfie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taghaza', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taghaza.Taghaza')),
            ],
            options={
                'verbose_name': 'تسویه',
                'verbose_name_plural': 'تسویه ها',
            },
        ),
    ]
