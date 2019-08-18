# Generated by Django 2.2.3 on 2019-07-19 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factor', '__first__'),
        ('sherkat', '__first__'),
        ('kala', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aghlam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mablagh', models.IntegerField(verbose_name='مبلغ واحد')),
                ('meghdar', models.IntegerField(verbose_name='مقدار')),
                ('makhs', models.SmallIntegerField()),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='factor.Factor', verbose_name='فاکتور')),
                ('kala', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kala.Kala', verbose_name='نام کالا')),
                ('sherkat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sherkat.Sherkat', verbose_name='تامین کننده')),
            ],
            options={
                'verbose_name': 'قلم',
                'verbose_name_plural': 'اقلام',
            },
        ),
    ]
