# Generated by Django 4.2.2 on 2023-07-02 10:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("health", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hospitalupload",
            old_name="email",
            new_name="Patient_Id",
        ),
    ]