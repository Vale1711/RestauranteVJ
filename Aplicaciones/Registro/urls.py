from django.urls import path
from . import views

urlpatterns=[
    path('', views.provincia, name='provincia'),
    path('guardarProvincia/', views.guardarProvincia),
    path('eliminarProvincia/<id_pro_vj>', views.eliminarProvincia),
    path('editarProvincia/<id_pro_vj>', views.editarProvincia),
    path('procesarinformacionProvincia/', views.procesarinformacionProvincia),
    path('ingrediente/', views.ingrediente, name='ingrediente'),
    path('guardarIngrediente/', views.guardarIngrediente),
    path('eliminarIngrediente/<id_in_vj>', views.eliminarIngrediente),
    path('editarIngrediente/<id_in_vj>', views.editarIngrediente),
    path('procesarinformacionIngrediente/', views.procesarinformacionIngrediente),
    path('cliente/', views.cliente, name='cliente'),
    path('guardarCliente/', views.guardarCliente),
    path('eliminarCliente/<id_cli_vj>', views.eliminarCliente),
    path('editarCliente/<id_cli_vj>', views.editarCliente),
    path('procesarinformacionCliente/', views.procesarinformacionCliente),
    path('pedido/', views.pedido, name='pedido'),
    path('guardarPedido/', views.guardarPedido),
    path('eliminarPedido/<id_pe_vj>', views.eliminarPedido),
    path('editarPedido/<id_pe_vj>', views.editarPedido),
    path('procesarinformacionPedido/', views.procesarinformacionPedido),
    path('tipo/', views.tipo, name='tipo'),
    path('guardarTipo/', views.guardarTipo),
    path('eliminarTipo/<id_ti_vj>', views.eliminarTipo),
    path('editarTipo/<id_ti_vj>', views.editarTipo),
    path('procesarinformacionTipo/', views.procesarinformacionTipo),
    path('platillo/', views.platillo, name='platillo'),
    path('guardarPlatillo/', views.guardarPlatillo),
    path('eliminarPlatillo/<id_pla_vj>', views.eliminarPlatillo),
    path('editarPlatillo/<id_pla_vj>', views.editarPlatillo),
    path('procesarinformacionPlatillo/', views.procesarinformacionPlatillo),
    path('detalle/', views.detalle, name='detalle'),
    path('guardarDetalle/', views.guardarDetalle),
    path('eliminarDetalle/<id_de_vj>', views.eliminarDetalle),
    path('editarDetalle/<id_de_vj>', views.editarDetalle),
    path('procesarinformacionDetalle/', views.procesarinformacionDetalle),
    path('receta/', views.receta, name='receta'),
    path('guardarReceta/', views.guardarReceta),
    path('eliminarReceta/<id_re_vj>', views.eliminarReceta),
    path('editarReceta/<id_re_vj>', views.editarReceta),
    path('procesarinformacionReceta/', views.procesarinformacionReceta),
]