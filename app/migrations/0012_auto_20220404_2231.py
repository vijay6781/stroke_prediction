# Generated by Django 3.2.7 on 2022-04-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220404_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='gnbstroke',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rfstroke',
            field=models.FloatField(blank=True, default=2, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='svmstroke',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]