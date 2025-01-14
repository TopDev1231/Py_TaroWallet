# Generated by Django 4.1.4 on 2023-02-10 09:40

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("walletapp", "0033_alter_transactions_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="currency",
            field=models.ForeignKey(
                blank=True,
                help_text="Transaction currency",
                on_delete=django.db.models.deletion.PROTECT,
                to="walletapp.currencies",
            ),
        ),
        migrations.CreateModel(
            name="PriceHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price_sat",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Currency price",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "time_stamp",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Timestamp",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        blank=True,
                        help_text="Currency for sale",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="walletapp.currencies",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Listings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price_sat",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="Price to sell the asset for",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        blank=True,
                        help_text="Asset for sale",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="walletapp.currencies",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="Internal user who has received the transaction",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
