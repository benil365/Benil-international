# Generated by Django 4.2.2 on 2023-07-12 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("health", "0004_alter_patient_registration_identity_no"),
    ]

    operations = [
       
        migrations.AlterField(
            model_name="hospitalupload",
            name="file",
            field=models.FileField(upload_to="uploads/"),
        ),
    ]
