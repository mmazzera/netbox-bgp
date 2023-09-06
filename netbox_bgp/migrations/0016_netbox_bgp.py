# Generated by Django 3.2 on 2021-05-07 09:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_bgp', '0015_netbox_bgp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='number',
        ),
        migrations.AlterField(
            model_name='asn',
            name='number',
            field=models.PositiveBigIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4294967294)]),
            preserve_default=False,
        ),
    ]
