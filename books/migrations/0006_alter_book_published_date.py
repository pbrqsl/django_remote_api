# Generated by Django 4.2.7 on 2023-11-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0005_book_published_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="published_date",
            field=models.CharField(max_length=10, null=True),
        ),
    ]