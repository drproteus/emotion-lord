# Generated by Django 3.0.2 on 2020-01-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='hello', max_length=256),
            preserve_default=False,
        ),
    ]
