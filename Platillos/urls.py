
from django.urls import path
from . import views
from .views import detalle_pedidos

urlpatterns=[
    path('', views.inicio, name='inicio'),
    #33333333333333333333333333333333
    path('provincia/',views.listadoProvincia),
    path('guardarProvincia/',views.guardarProvincia),
    path('eliminarProvincia/<id_jt>',views.eliminarProvincia),
    path('editarProvincia/<id_jt>',views.editarProvincia),
    path('procesarActualizacionProvincia/<id_jt>',views.procesarActualizacionProvincia, name='procesarActualizacionProvincia'),
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    path('cliente/',views.listadoCliente),
    path('guardarCliente/',views.guardarCliente),
    path('eliminarCliente/<id_jt>',views.eliminarCliente),
    path('editarCliente/<id_jt>',views.editarCliente),
    path('procesarActualizacionCliente/<id_jt>',views.procesarActualizacionCliente, name='procesarActualizacionCliente'),
    ######################
    path('pedido/',views.listadoPedido),
    path('guardarPedido/',views.guardarPedido),
    path('eliminarPedido/<idPedido_jt>',views.eliminarPedido),
    path('editarPedido/<idPedido_jt>',views.editarPedido),
    path('procesarActualizacionPedido/<idPedido_jt>',views.procesarActualizacionPedido, name='procesarActualizacionPedido'),
    #$$$$$$$$$$$$$$$$$$$
    path('tipo/',views.listadoTipo),
    path('guardarTipo/',views.guardarTipo),
    path('eliminarTipo/<idTipo_jt>',views.eliminarTipo),
    path('editarTipo/<idTipo_jt>',views.editarTipo),
    path('procesarActualizacionTipo/<idTipo_jt>',views.procesarActualizacionTipo, name='procesarActualizacionTipo'),
    #$$$$$$$$$$$$$$$$
    path('platillo/',views.listadoPlatillo),
    path('guardarPlatillo/',views.guardarPlatillo),
    path('eliminarPlatillo/<idPlatillo_jt>',views.eliminarPlatillo),
    path('editarPlatillo/<idPlatillo_jt>',views.editarPlatillo),
    path('procesarActualizacionPlatillo/<idPlatillo_jt>',views.procesarActualizacionPlatillo, name='procesarActualizacionPlatillo'),
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    path('ingrediente/',views.listadoIngrediente),
    path('guardarIngrediente/',views.guardarIngrediente),
    path('eliminarIngrediente/<idIngrediente_jt>',views.eliminarIngrediente),
    path('editarIngrediente/<idIngrediente_jt>',views.editarIngrediente),
    path('procesarActualizacionIngrediente/<idIngrediente_jt>',views.procesarActualizacionIngrediente, name='procesarActualizacionIngrediente'),
    #33333333333333333333333333333333
    path('receta/',views.listadoReceta),
    path('guardarReceta/',views.guardarReceta),
    path('eliminarReceta/<idReceta_jt>',views.eliminarReceta),
    path('editarReceta/<idReceta_jt>',views.editarReceta),
    path('procesarActualizacionReceta/<idReceta_jt>',views.procesarActualizacionReceta, name='procesarActualizacionReceta'),
    #$$$$$$$$$$$$$$$$$
    path('detalle_pedidos/', detalle_pedidos, name='detalle_pedidos'),


]
