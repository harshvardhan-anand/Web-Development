# Generated by Django 3.1.1 on 2020-11-07 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_auto_20201107_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='abc',
            new_name='name',
        ),
    ]
