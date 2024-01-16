from django.db import models
from datetime import datetime


class Provincia(models.Model):
    id_jt = models.AutoField(primary_key=True)
    region_jt = models.CharField(max_length=150)
    nombre_jt = models.CharField(max_length=150)
    capital_jt = models.CharField(max_length=150)
    ciudad_jt = models.CharField(max_length=150)

    def __str__(self):
        fila = "id_jt: {0}-{1}-{2}-{3}"
        return fila.format(self.id_jt, self.region_jt, self.nombre_jt, self.capital_jt, self.ciudad_jt)

class Cliente(models.Model):
    id_jt = models.AutoField(primary_key=True)
    cedula_jt = models.CharField(max_length=10)
    apellido_jt = models.CharField(max_length=150)
    nombre_jt = models.CharField(max_length=150, null=True, default='ValorPredeterminado')
    provincia = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.PROTECT)
    direccion_jt = models.TextField()
    fecha_nacimiento_jt = models.DateField()
    correo_jt = models.EmailField()

    def __str__(self):
        fila = "id_jt: {0}-{1}-{2}-{3}"
        return fila.format(self.id_jt, self.cedula_jt, self.apellido_jt, self.nombre_jt, self.correo_jt)




class Tipo(models.Model):
    idTipo_jt = models.AutoField(primary_key=True)
    nombreTipo_jt = models.CharField(max_length=150)
    descripcionTipo_jt = models.TextField()
    categoriaTipo_jt = models.CharField(max_length=150)


    def __str__(self):
        fila = "idTipo_jt: {0}-{1}-{2}-{3}"
        return fila.format(self.idTipo_jt, self.nombreTipo_jt, self.descripcionTipo_jt, self.categoriaTipo_jt)



class Platillo(models.Model):
    idPlatillo_jt = models.AutoField(primary_key=True)
    nombrePlatillo_jt = models.CharField(max_length=150)
    tipo= models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.PROTECT)
    descripcionPlatillo_jt = models.TextField()
    precioPlatillo_jt = models.DecimalField(max_digits=10, decimal_places=2)


def __str__(self):
    fila = "idPlatillo_jt: {0}-{1}-{2}-{3}-{4}"
    return fila.format(self.idPlatillo_jt, self.nombrePlatillo_jt, self.tipo, self.descripcionPlatillo_jt, self.precioPlatillo_jt)

class Pedido(models.Model):
    idPedido_jt = models.AutoField(primary_key=True)
    nombre = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.PROTECT)
    tipo= models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.PROTECT)
    platillo= models.ForeignKey(Platillo, null=True, blank=True, on_delete=models.PROTECT)
    fechaPedido_jt = models.DateField()
    descripcionPedido_jt = models.TextField()
    horaPedido_jt = models.TimeField(default=datetime.now)
    fotografiaPedido_jt = models.ImageField(upload_to='pedidos', null=True, blank=True)


    def __str__(self):
        fila = "idPedido_jt: {0}-{1}-{2}-{3}"
        return fila.format(self.idPedido_jt, self.nombre ,self.fechaPedido_jt, self.descripcionPedido_jt, self.horaPedido_jt)

class Ingrediente(models.Model):
    idIngrediente_jt = models.AutoField(primary_key=True)
    nombreIngrediente_jt = models.CharField(max_length=150)
    fechaExpiracion_jt = models.DateField()
    fotografiaIngrediente_jt = models.ImageField(upload_to='ingredientes', null=True, blank=True)


def __str__(self):
    fila = "idPlatillo_jt: {0}-{1}-{2}-{3}"
    return fila.format(self.idIngrediente_jt, self.nombreIngrediente_jt, self.fechaExpiracion_jt, self.fotografiaIngrediente_jt)

class Receta(models.Model):
    idReceta_jt = models.AutoField(primary_key=True)
    platillo= models.ForeignKey(Platillo, null=True, blank=True, on_delete=models.PROTECT)
    ingrediente= models.ForeignKey(Ingrediente, null=True, blank=True, on_delete=models.PROTECT)
    pasosReceta_jt= models.TextField()
    tiempoPreparacion_jt = models.IntegerField()
    dificultadReceta_jt = models.CharField(max_length=50)


    def __str__(self):
        fila = "idReceta_jt: {0}-{1}-{2}-{3}"
        return fila.format(self.idReceta_jt, self.platillo ,self.ingrediente, self.pasosReceta_jt, self.tiempoPreparacion_jt)



class Detalle(models.Model):
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return f"Detalle: {self.id} "
