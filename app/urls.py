"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categoria_rest', views.CategoriaRestViewSet)
router.register('producto_rest', views.ProductoViewSet)
router.register('mesero_rest', views.MeseroViewSet)
router.register('cliente_rest', views.ClienteViewSet)
router.register('factura_rest', views.FacturaViewSet)


urlpatterns = [

    path('api/', include(router.urls)),

    path('', views.first_view, name='base'),
    
    #categoria
    path('categoria/', views.categoria, name='categoria-list'), 
    path('categoria/<int:categoria_id>/detalle/', views.categoria_detalle, name='categoria-detalle'),
    path('categoria/<int:pk>/update/', views.CategoriaUpdate.as_view(), name='categoria-update'),
    path('categoria/create/', views.CategoriaCreate.as_view(), name='categoria-create'),
    path('categoria/<int:pk>/delete/', views.CategoriaDelete.as_view(), name='categoria-delete'),

    #productos
    path('producto/', views.ProductoListView.as_view(), name='producto-list'),
    path('producto/<int:pk>/detail/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/<int:pk>/update/', views.ProductoUpdate.as_view(), name='producto-update'),
    path('producto/create/', views.ProductoCreate.as_view(), name='producto-create'),
    path('producto/<int:pk>/delete/', views.ProductoDelete.as_view(), name='producto-delete'),

    #clientes
    path('cliente/', views.ClienteListView.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/detail/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente-update'),
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente-create'),
    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente-delete'),

    #meseros
    path('mesero/', views.MeseroListView.as_view(), name='mesero-list'),
    path('mesero/<int:pk>/detail/', views.MeseroDetailView.as_view(), name='mesero-detail'),
    path('mesero/<int:pk>/update/', views.MeseroUpdate.as_view(), name='mesero-update'),
    path('mesero/create/', views.MeseroCreate.as_view(), name='mesero-create'),
    path('mesero/<int:pk>/delete/', views.MeseroDelete.as_view(), name='mesero-delete'),

    #factura
    path('factura/', views.FacturaListView.as_view(), name='factura-list'),
    path('factura/<int:pk>/detail/', views.FacturaDetailView.as_view(), name='factura-detail'),
    path('factura/<int:pk>/update/', views.FacturaUpdate.as_view(), name='factura-update'),
    path('factura/create/', views.FacturaCreate.as_view(), name='factura-create'),
    path('factura/<int:pk>/delete/', views.FacturaDelete.as_view(), name='factura-delete'),

]
