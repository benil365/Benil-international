# Generated by Django 4.2.2 on 2023-07-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("health", "0003_remove_patient_registration_residence_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient_registration",
            name="Identity_No",
            field=models.IntegerField(null=True),
        ),
    ]
