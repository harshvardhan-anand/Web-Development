# Generated by Django 3.1.1 on 2020-11-07 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_auto_20201107_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='abc',
        ),
    ]