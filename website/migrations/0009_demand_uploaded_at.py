# Generated by Django 3.0.3 on 2020-03-04 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200304_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
