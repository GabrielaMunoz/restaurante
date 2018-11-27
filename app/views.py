from django.shortcuts import render
from django.http import HttpResponse 
from app.models import Producto, Mesero, Cliente, Factura, Categoria
from django.views.generic import ListView, DetailView 
from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, MeseroSerializer, FacturaSerializer
from datetime import *
from django.template import RequestContext as ctx
from datetime import datetime
from django.shortcuts import render_to_response

@login_required
def first_view(request):
    return render(request, 'base.html')

# Create your views here.
@login_required
def factura_detail(request, pk):
    compra = Factura.objects.get(pk=pk)
    context = {'object': compra}
    fields = '__all__'
    hora = datetime.today()
    return render(request, 'app/factura_detail.html', context)

#----------------------FACTURA--------------------------
@method_decorator(login_required, name='dispatch')
class FacturaListView(ListView):
    model=Factura
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FacturaDetailView(DetailView):
    model = Factura
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class FacturaUpdate(UpdateView):
    model = Factura
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FacturaCreate(CreateView):
    model = Factura
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FacturaDelete(DeleteView):
    model = Factura
    success_url = reverse_lazy('factura-list')

"""
@login_required
def factura_detalle(request, id_factura_id):
    detalles = DetalleFactura.objects.get(id=id_factura_id)
    context= {'object': detalles}
    return render( request, 'app/factura_detail.html', context)"""
#----------------------CATEGORIA--------------------------
@login_required
def categoria(request):
    categoria_list = Categoria.objects.all()
    context = {'object_list': categoria_list}
    return render(request, 'app/categoria.html', context)

#permite editar la categoria 
@login_required
def categoria_detalle(request, categoria_id):
 categoria = Categoria.objects.get(id=categoria_id)
 context = {'object': categoria}
 return render(request, 'app/categoria_detalle.html', context)

@method_decorator(login_required, name='dispatch')
class CategoriaUpdate(UpdateView):

    model=Categoria
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class CategoriaCreate(CreateView):
     
     model=Categoria
     fields = '__all__'
 
@method_decorator(login_required, name='dispatch')
class CategoriaDelete(DeleteView):

    model=Categoria
    success_url = reverse_lazy('categoria-list')

#----------------------PRODUCTO--------------------------
@method_decorator(login_required, name='dispatch')
class ProductoListView(ListView):
    model = Producto

@method_decorator(login_required, name='dispatch')
class ProductoDetailView(DetailView):
    model = Producto

@method_decorator(login_required, name='dispatch')
class ProductoUpdate(UpdateView):
    model = Producto
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')


#----------------------CLIENTE--------------------------
@method_decorator(login_required, name='dispatch')
class ClienteListView(ListView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteDetailView(DetailView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteCreate(CreateView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente-list')


#----------------------MESERO--------------------------
@method_decorator(login_required, name='dispatch')
class MeseroListView(ListView):
    model=Mesero
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MeseroDetailView(DetailView):
    model=Mesero
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MeseroUpdate(UpdateView):
    model=Mesero
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MeseroCreate(CreateView):
    model=Mesero
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MeseroDelete(DeleteView):
    model = Mesero
    success_url = reverse_lazy('mesero-list')


#----------------------SERIALIZER--------------------------

#@method_decorator(login_required, name='dispatch')
class CategoriaRestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#@method_decorator(login_required, name='dispatch')
class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#@method_decorator(login_required, name='dispatch')
class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

#@method_decorator(login_required, name='dispatch')
class MeseroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mesero.objects.all()
    serializer_class = MeseroSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
