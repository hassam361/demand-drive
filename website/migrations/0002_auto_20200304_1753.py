# Generated by Django 3.0.3 on 2020-03-04 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demand',
            old_name='content',
            new_name='description',
        ),
    ]
