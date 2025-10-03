from dataclasses import dataclass, field 
from typing import List 
from modelos import Cliente, LineaFactura, Producto 
from descuentos import Descuento
from impuestos import Impuesto

@dataclass 
class Factura:
    cliente: Cliente 
    lineas: List[LineaFactura] = field(default_factory=list)

    def agregar_linea(self, producto: Producto, cantidad = 1):
        self.lineas.append(LineaFactura(producto, cantidad))

    def calcular_descuentos(self, descuento: Descuento):
        return sum(descuento.aplicar(self.cliente, 1) for l in self.lineas)
    
    def calcular_impuestos(self, impuesto: Impuesto):
        return sum(impuesto.calcular(self.cliente, 1) for l in self.lineas)
    
    def calcular_total(self, impuesto: Impuesto, descuento: Descuento):
        return sum(l.subtotal for l in self.lineas) + self.calcular_impuestos(impuesto) - self.calcular_descuentos(descuento)
    


    
