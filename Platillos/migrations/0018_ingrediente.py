# Generated by Django 4.2.7 on 2024-01-16 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0017_platillo_pedido_fotografiapedido_jt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('idIngrediente_jt', models.AutoField(primary_key=True, serialize=False)),
                ('nombreIngrediente_jt', models.CharField(max_length=150)),
                ('fechaExpiracion_jt', models.DateField()),
                ('fotografiaIngrediente_jt', models.ImageField(blank=True, null=True, upload_to='ingredientes')),
            ],
        ),
    ]
