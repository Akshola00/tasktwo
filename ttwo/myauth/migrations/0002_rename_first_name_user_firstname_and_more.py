# Generated by Django 5.0.6 on 2024-07-07 15:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myauth", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="first_name",
            new_name="firstName",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="last_name",
            new_name="lastName",
        ),
    ]
