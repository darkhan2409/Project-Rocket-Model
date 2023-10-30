# Generated by Django 4.2.6 on 2023-10-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0006_remove_rocket_manned_alter_rocket_fuel_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rocket',
            name='fuel_condition',
            field=models.CharField(blank=True, choices=[('Solid rocket engine', 'SRE'), ('Liquid rocket engine', 'Liquid rocket engine'), ('Hybrid', 'Hybrid')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rocket',
            name='type',
            field=models.CharField(blank=True, choices=[('Lightweight – up to 5 tons of payload', 'Light'), ('Medium - from 5 to 20 tons', 'Medium'), ('Heavy – from 20 to 100 tons', 'Heavy'), ('Super heavy – over 100 tons', 'Super heavy')], max_length=50, null=True),
        ),
    ]