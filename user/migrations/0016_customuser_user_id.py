# Generated by Django 4.2.2 on 2025-01-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0015_customuser_name_customuser_reg_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="user_id",
            field=models.IntegerField(null=True),
        ),
    ]
