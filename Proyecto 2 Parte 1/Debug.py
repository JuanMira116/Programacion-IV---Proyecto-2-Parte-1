
from datetime import date
from decimal import Decimal
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.antibiotico import Antibiotico
from modelo.control_fertilizantes import ControlDeFertilizantes
from modelo.control_plagas import ControlDePlagas

cliente = Cliente("Juan Pérez", "12345")

antibiotico = Antibiotico("Amoxicilina", 500, "Bovino", Decimal("15000"))
fertilizante = ControlDeFertilizantes("ICA123", "FertiMax", "Cada 30 días", date.today(), Decimal("40000"))
plaguicida = ControlDePlagas("ICA999", "PlagaKill", "Cada 15 días", 7, Decimal("30000"))

factura = Factura(date.today())

factura.agregar_producto(antibiotico)
factura.agregar_producto(fertilizante)
factura.agregar_producto(plaguicida)
cliente.agregar_factura(factura)

print("=== Datos del cliente ===")
print(f"Nombre: {cliente.nombre}")
print(f"Cédula: {cliente.cedula}")
print(f"Número de facturas: {len(cliente.facturas)}")

print("\n=== Factura ===")
print(f"Fecha: {factura.fecha}")
print("Productos comprados:")
for p in factura.productos:
    print(f" - {p.nombre}: ${p.precio:.2f}")
print(f"Total factura: ${factura.valor_total:.2f}")

print("\nListo para debug")