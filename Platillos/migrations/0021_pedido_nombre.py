# Generated by Django 4.2.7 on 2024-01-16 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0020_cliente_provincia_alter_cliente_nombre_jt'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='nombre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Platillos.cliente'),
        ),
    ]
