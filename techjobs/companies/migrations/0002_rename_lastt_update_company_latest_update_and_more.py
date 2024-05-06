# Generated by Django 5.0.4 on 2024-05-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="company",
            old_name="lastt_update",
            new_name="latest_update",
        ),
        migrations.AddField(
            model_name="company",
            name="application_link",
            field=models.URLField(max_length=500, null=True),
        ),
    ]
