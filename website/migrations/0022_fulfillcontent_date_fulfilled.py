# Generated by Django 3.0.3 on 2020-03-21 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20200321_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfillcontent',
            name='date_fulfilled',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
