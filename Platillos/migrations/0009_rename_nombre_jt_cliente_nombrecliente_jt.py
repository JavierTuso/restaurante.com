# Generated by Django 4.2.7 on 2024-01-15 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0008_rename_id_cliente_id_jt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre_jt',
            new_name='nombreCliente_jt',
        ),
    ]
