# Generated by Django 4.1.4 on 2023-11-21 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0060_alter_currencies_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="currencies",
            options={
                "ordering": [
                    "-holders_num",
                    "-transaction_num",
                    "-orders_num",
                    "-volume",
                ]
            },
        ),
        migrations.AlterField(
            model_name="currencies",
            name="supply",
            field=models.BigIntegerField(
                blank=True,
                default=1,
                help_text="Total supply of the asset once minted",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(4294967296),
                ],
            ),
        ),
    ]