# Generated by Django 3.0.3 on 2020-03-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_demand_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfillcontent',
            name='user_likes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
