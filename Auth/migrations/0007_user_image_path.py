# Generated by Django 4.2.2 on 2023-06-29 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0006_level_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_path',
            field=models.CharField(max_length=50, null=True),
        ),
    ]