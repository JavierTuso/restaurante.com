# Generated by Django 4.2.7 on 2024-01-16 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0021_pedido_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Platillos.tipo'),
        ),
    ]
