from django.shortcuts import render
from models import Cliente
from django.http import HttpResponse

"""cliente = Cliente(nombre="Supermaren", formadepago="credito", tienedeuda=False)
cliente.save()"""

def cliente(self):
    cliente=Cliente(nombre="Megamax",formadepago="Credito", tienedeuda=False)
    cliente.save()
    documentoDeTexto=f"--->Cliente:{cliente.nombre},Cliente{cliente.formadepago},Cliente{cliente.tienedeuda}"
    return HttpResponse(documentoDeTexto)