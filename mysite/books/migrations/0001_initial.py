# Generated by Django 2.2.6 on 2022-10-09 08:36

from django.db import migrations, models
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('publisher', models.CharField(max_length=100)),
                ('isbn', isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
            ],
        ),
    ]