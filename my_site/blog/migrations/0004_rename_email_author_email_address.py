# Generated by Django 4.2.7 on 2023-12-04 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_img_name_post_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='email',
            new_name='email_address',
        ),
    ]