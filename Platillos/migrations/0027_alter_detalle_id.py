# Generated by Django 4.2.7 on 2024-01-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platillos', '0026_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
