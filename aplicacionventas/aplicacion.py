from modelos import Producto, Cliente 
from pedido import Factura 
from descuentos import DescuentoVIP, DescentoVolumen
from impuestos import IVA, Excentos 

cliente = Cliente(123, "Juan", False)
producto1 = Producto(567, "Arepas", "alimentos", 2000)
producto2 = Producto(949, "suscripcion netflix", "aservicios", 25000)
producto3 = Producto(111, "computador", "tecnologia", 2500000)

mifactura = Factura(cliente)

mifactura.agregar_linea(producto1, 10)

descuento_a_aplicar = DescentoVolumen()
impuesto_a_aplicar = IVA()

print(mifactura.calcular_total(descuento_a_aplicar, impuesto_a_aplicar))
