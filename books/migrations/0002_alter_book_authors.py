# Generated by Django 4.2.7 on 2023-11-05 20:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True, default=0, max_length=100, null=True
                ),
                size=None,
            ),
        ),
    ]
