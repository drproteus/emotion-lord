# Generated by Django 3.0.2 on 2020-01-06 21:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moodrecord",
            name="id",
            field=models.CharField(
                default=uuid.uuid4, max_length=256, primary_key=True, serialize=False
            ),
        ),
    ]