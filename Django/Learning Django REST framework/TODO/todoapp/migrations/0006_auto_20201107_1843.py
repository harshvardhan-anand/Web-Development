# Generated by Django 3.1.1 on 2020-11-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20201107_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(default='', max_length=10),
        ),
    ]
