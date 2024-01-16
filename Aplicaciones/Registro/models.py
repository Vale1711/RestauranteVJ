from django.db import models

class Provincia(models.Model):
    id_pro_vj=models.AutoField(primary_key=True)
    nombre_vj=models.CharField(max_length=100)
    region_vj=models.CharField(max_length=150)
    capital_vj=models.CharField(max_length=150)
    descripcion_vj=models.CharField(max_length=150)

class Ingrediente(models.Model):
    id_in_vj=models.AutoField(primary_key=True)
    nombre_vj=models.CharField(max_length=100)
    categoria_vj=models.CharField(max_length=150)
    fechacadu_vj=models.DateField()
    precio_vj=models.CharField(max_length=10)
    imagen_in_vj=models.FileField(upload_to='ingredientes', null=True, blank=True)

class Cliente(models.Model):
    id_cli_vj=models.AutoField(primary_key=True)
    cedula_vj=models.CharField(max_length=100)
    apellido_vj=models.CharField(max_length=150)
    nombre_vj=models.CharField(max_length=150)
    direccion_vj=models.CharField(max_length=150)
    provincia_vj=models.ForeignKey(Provincia,null=True,blank=True,on_delete=models.CASCADE)

class Pedido(models.Model):
    id_pe_vj=models.AutoField(primary_key=True)
    fechape_vj=models.DateField()
    estadope_vj=models.CharField(max_length=150)
    metodopago_vj=models.CharField(max_length=150)
    observacion_vj=models.CharField(max_length=150)
    cliente_vj=models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)

class Tipo(models.Model):
    id_ti_vj=models.AutoField(primary_key=True)
    nombre_vj=models.CharField(max_length=150)
    descripcion_vj=models.CharField(max_length=150)
    categoria_vj=models.CharField(max_length=150)


class Platillo(models.Model):
    id_pla_vj=models.AutoField(primary_key=True)
    nombre_vj=models.CharField(max_length=150)
    calorias_vj=models.CharField(max_length=150)
    descripcion_vj=models.CharField(max_length=150)
    imagen_pla_vj=models.FileField(upload_to='platillos', null=True, blank=True)
    tipo_vj=models.ForeignKey(Tipo,null=True,blank=True,on_delete=models.CASCADE)


class Detalle(models.Model):
    id_de_vj=models.AutoField(primary_key=True)
    cantidad_vj=models.CharField(max_length=10)
    preciounitario_vj=models.CharField(max_length=10)
    descuento_vj=models.CharField(max_length=10)
    total_vj=models.CharField(max_length=10)
    pedido_vj=models.ForeignKey(Pedido,null=True,blank=True,on_delete=models.CASCADE)
    platillo_vj=models.ForeignKey(Platillo,null=True,blank=True,on_delete=models.CASCADE)

class Receta(models.Model):
    id_re_vj=models.AutoField(primary_key=True)
    nombre_vj=models.CharField(max_length=150)
    tiempoprepa_vj=models.CharField(max_length=150)
    dificultad_vj=models.CharField(max_length=150)
    descripcion_vj=models.CharField(max_length=150)
    platillo_vj=models.ForeignKey(Platillo,null=True,blank=True,on_delete=models.CASCADE)
    ingrediente_vj=models.ForeignKey(Ingrediente,null=True,blank=True,on_delete=models.CASCADE)
