# Generated by Django 4.2.2 on 2023-08-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_patient_hospital"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Hospital",
            new_name="Doctor",
        ),
        migrations.RenameModel(
            old_name="HospitalData",
            new_name="DoctorData",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("doctor", "Doctor"), ("patient", "Patient")], max_length=20
            ),
        ),
    ]
