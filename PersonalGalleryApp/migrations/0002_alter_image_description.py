# Generated by Django 3.2.8 on 2021-10-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalGalleryApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(),
        ),
    ]
