# Generated by Django 4.1.4 on 2023-11-01 22:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0053_alter_currencies_acronym_alter_currencies_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currencies",
            name="acronym",
            field=models.CharField(
                help_text="Asset acronym represented as 1 to 5 letters. e.g. ETH, BTC",
                max_length=5,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
                    )
                ],
            ),
        ),
    ]