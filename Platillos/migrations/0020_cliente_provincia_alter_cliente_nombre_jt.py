# Generated by Django 4.2.7 on 2024-01-16 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0019_alter_cliente_nombre_jt'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Platillos.provincia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_jt',
            field=models.CharField(default='ValorPredeterminado', max_length=150, null=True),
        ),
    ]
