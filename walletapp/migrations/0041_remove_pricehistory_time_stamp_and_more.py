# Generated by Django 4.1.4 on 2023-02-13 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0040_alter_pricehistory_currency"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pricehistory",
            name="time_stamp",
        ),
        migrations.AddField(
            model_name="pricehistory",
            name="created_timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="pricehistory",
            name="period",
            field=models.CharField(
                blank=True,
                choices=[("1m", "1 minute"), ("1h", "1 hour"), ("1d", "1 day")],
                help_text="Time period",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="listings",
            name="currency",
            field=models.ForeignKey(
                blank=True,
                help_text="Asset for sale",
                on_delete=django.db.models.deletion.CASCADE,
                to="walletapp.currencies",
                unique=True,
            ),
        ),
    ]