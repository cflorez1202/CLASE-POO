from dataclasses import dataclass, field 
from typing import List

@dataclass 
class Producto:
    codigo: int 
    nombre: str
    categorias: str 
    precio: float 

class Cliente:
    id: int
    nombre: str
    vip: bool

@dataclass
class LineaFactura:
    producto: Producto
    cantidad: int

    @property
    def subtotal(self) -> float:
        return self.producto.precio * self.cantidad
    
    

