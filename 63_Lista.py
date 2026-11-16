from rich.table import Table

from Rich import console

table = Table(title="Lista de la compra")
table.add_column("Producto", style="cyan")
table.add_column("Cantidad", justify="right")
table.add_row("Huevos", "6")
table.add_row("Patatas", "4")
table.add_row("Cebolla", "1")
console.print(table)
