# Generated by Django 5.0.6 on 2024-07-07 17:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myauth", "0003_rename_user_id_user_userid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="userId",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]