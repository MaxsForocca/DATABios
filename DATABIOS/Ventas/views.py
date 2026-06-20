from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def ventas_list(request):
    raise Http404("El módulo de Ventas está deshabilitado temporalmente.")

@login_required
def detalle_venta(request, venta_id):
    raise Http404("El módulo de Ventas está deshabilitado temporalmente.")

@login_required
def agregar_venta(request):
    raise Http404("El módulo de Ventas está deshabilitado temporalmente.")

@login_required
def agregar_producto_venta(request):
    raise Http404("El módulo de Ventas está deshabilitado temporalmente.")

@login_required
def eliminar_venta(request, venta_id):
    raise Http404("El módulo de Ventas está deshabilitado temporalmente.")

@login_required
def crear_excel(request):
    raise Http404("El módulo de Ventas está deshabilitado temporalmente.")
