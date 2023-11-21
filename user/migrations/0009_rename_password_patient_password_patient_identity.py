# Generated by Django 4.2.2 on 2023-09-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0008_alter_doctordata_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="patient",
            old_name="Password",
            new_name="password",
        ),
        migrations.AddField(
            model_name="patient",
            name="identity",
            field=models.CharField(default="", max_length=10, unique=True),
        ),
    ]
