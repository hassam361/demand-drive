# Generated by Django 3.0.3 on 2020-03-04 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200304_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='items',
            field=models.FileField(default=django.utils.timezone.now, upload_to='contents/'),
            preserve_default=False,
        ),
    ]