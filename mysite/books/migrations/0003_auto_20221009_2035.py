# Generated by Django 2.2.6 on 2022-10-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20221009_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]