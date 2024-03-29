# Generated by Django 4.2.7 on 2024-01-16 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0012_rename_apellidocliente_jt_cliente_apellido_jt_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='idCliente_jt',
            new_name='id_jt',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='id_jt',
            new_name='idPedido_jt',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fotografiaPedido_jt',
            field=models.ImageField(blank=True, null=True, upload_to='pedidos'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='horaPedido_jt',
            field=models.TimeField(),
        ),
    ]
