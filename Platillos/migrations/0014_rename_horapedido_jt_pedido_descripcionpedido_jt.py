# Generated by Django 4.2.7 on 2024-01-16 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0013_rename_idcliente_jt_cliente_id_jt_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='horaPedido_jt',
            new_name='descripcionPedido_jt',
        ),
    ]