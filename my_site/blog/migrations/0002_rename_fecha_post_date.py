# Generated by Django 4.2.7 on 2023-12-04 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='fecha',
            new_name='date',
        ),
    ]
