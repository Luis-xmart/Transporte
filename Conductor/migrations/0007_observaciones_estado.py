# Generated by Django 4.0.2 on 2022-05-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conductor', '0006_remove_observaciones_entrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='observaciones',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
