# Generated by Django 4.2.2 on 2023-08-30 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_rename_hospital_doctordata_doctor"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctordata",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
