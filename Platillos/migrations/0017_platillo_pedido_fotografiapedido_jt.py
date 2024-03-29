# Generated by Django 4.2.7 on 2024-01-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0016_tipo_remove_pedido_fotografiapedido_jt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('idPlatillo_jt', models.AutoField(primary_key=True, serialize=False)),
                ('nombrePLatillo_jt', models.CharField(max_length=150)),
                ('descripcionPlatillo_jt', models.TextField()),
                ('precioPlatillo_jt', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='fotografiaPedido_jt',
            field=models.ImageField(blank=True, null=True, upload_to='pedidos'),
        ),
    ]
