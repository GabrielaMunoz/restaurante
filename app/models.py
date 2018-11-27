from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver 
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):

    nombre=models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre
        
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('categoria-list')

class Producto(models.Model):

    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50, default='No title')
    precio = models.CharField(max_length=50)
    producto = models.ImageField(upload_to='producto/')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('producto-list')

    def __str__(self):
        return self.titulo
        

class Mesero(models.Model):

    #id = models.CharField(max_length=50, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipo_de_documento = models.CharField(max_length=50)
    numero_de_documento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombres+" "+self.apellidos
    
    def get_absolute_url(self):
        return reverse('mesero-list')

class Cliente(models.Model):

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipo_de_documento = models.CharField(max_length=50)
    numero_de_documento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombres+" "+self.apellidos
    
    def get_absolute_url(self):
        return reverse('cliente-list')

class Factura(models.Model):

    id_cliente = models.ForeignKey( 'Cliente',on_delete=models.PROTECT)
    id_mesero = models.ForeignKey( 'Mesero',on_delete=models.PROTECT)
    id_producto = models.ForeignKey( 'Producto',on_delete=models.PROTECT)
    serie = models.IntegerField()
    numero = models.CharField(max_length=6)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
   
    def __str__(self):
        return self.numero

    def get_absolute_url(self):
        return reverse('factura-list')


"""
class DetalleFactura(models.Model):
    
    id_factura= models.ForeignKey( 'Factura',on_delete=models.PROTECT)
    id_producto= models.ForeignKey( 'Producto',on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()
    impuesto = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return u'%s' % self.descripcion

    def suma(self):
        return self.cantidad * self.producto.precio_venta

def update_stock(sender, instance, **kwargs):
    instance.producto.stock -= instance.cantidad
    instance.producto.save()

 #register the signal
    signals.post_save.connect(update_stock, sender=DetalleFactura, dispatch_uid="update_stock_count")"""

@receiver(post_delete, sender=Producto)
def producto_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.producto.delete(False)