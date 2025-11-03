
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.item_factura import ItemFactura
from modelo.antibiotico import Antibiotico
from modelo.tipo_animal import TipoAnimal
from datetime import date

cliente = Cliente("Juan Pérez", "12345")
antib = Antibiotico("Amoxicilina", 500, TipoAnimal.BOVINO, 15000)
factura = Factura(date.today())
item = ItemFactura(antib, 2)

factura.agregar_item(item)
cliente.agregar_factura(factura)

print("Listo para debug")