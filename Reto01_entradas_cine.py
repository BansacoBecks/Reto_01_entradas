from rich.console import Console
from rich.table import Table

console = Console()
console.print("\n[bold cyan]ENTRADAS CINE[/bold cyan]\n")
precio_base= 8.0
edad = int(input("Introduce tu edad: "))
presupuesto = float(input("Presupuesto disponible (EUR): "))
cantidad = (int(input("Numero de entradas: ")))

if edad<12:
    porcentaje_descuento = 50
elif edad>=65:
    porcentaje_descuento = 25
else:
    porcentaje_descuento = 0
descuento_euros = precio_base*porcentaje_descuento/100
precio_final= precio_base- descuento_euros
total = precio_final * cantidad
tabla = Table(title="Resumen de la compra")
tabla.add_column("Concepto", style="cyan")
tabla.add_column("Valor", style="green")
tabla.add_row("Edad",str(edad))
tabla.add_row("Cantidad de entradas",str(cantidad))
tabla.add_row("Precio base",f"{precio_base:.2f}EUR")
tabla.add_row("Descuento",f"{porcentaje_descuento}%")
tabla.add_row("Descuento por entrada",f"{descuento_euros:.2f}EUR")
tabla.add_row("Precio final por entrada",f"{precio_final:.2f}EUR")
tabla.add_row("Presupuesto",f"{presupuesto:.2f}EUR")
tabla.add_row("Total",f"{total:.2f}EUR")
console.print(tabla)
if presupuesto>=total:
    dinero_sobrante = presupuesto-total
    console.print(f"\n[bold green]Compra posible. Sobran{dinero_sobrante:.2f}EUR.[/bold green]")
else:
    dinero_faltante = total-presupuesto
    console.print(f"\n[bold red]Presupuesto insuficiente. Faltan{dinero_faltante:.2f} EUR.[/bold red]")





