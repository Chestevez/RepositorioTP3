from .Clientes import Cliente
from .Proveedores import Proveedor

class Comprobante:
    def __init__(self, numero, fecha, cliente, proveedor, kg, tarifa):
        self.numero = numero
        self.fecha = fecha
        self.cliente = cliente
        self.proveedor = proveedor
        self.kg = kg
        self.tarifa = tarifa
        self.importe_total = self.calcular_total()
    
    def calcular_total(self):
        return self.kg * self.tarifa