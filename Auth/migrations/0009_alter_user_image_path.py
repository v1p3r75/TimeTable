# Generated by Django 4.2.2 on 2023-06-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0008_alter_user_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_path',
            field=models.CharField(default='default.svg', max_length=50),
        ),
    ]
