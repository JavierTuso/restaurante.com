# Generated by Django 4.2.7 on 2024-01-15 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0006_alter_cliente_nombre_jt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='id_jt',
            new_name='id',
        ),
    ]