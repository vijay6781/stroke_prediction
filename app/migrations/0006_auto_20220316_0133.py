# Generated by Django 3.2.7 on 2022-03-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_record_overallresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='dtstroke',
            field=models.FloatField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='knnstroke',
            field=models.FloatField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='lrstroke',
            field=models.FloatField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rfstroke',
            field=models.FloatField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='svmstroke',
            field=models.FloatField(blank=True, default=5, null=True),
        ),
    ]
