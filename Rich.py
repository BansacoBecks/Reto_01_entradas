from rich import print
print("[bold green]Operacion correcta[/bold green]")
print("[red]Error: dato incorrect[/red]")
print("[underline]texto subrayado[/underline]")
from rich.console import Console
console = Console()
console.print("Cuidado", style="bold yellow")
console.print("Error", style="bold white on red")
console.print("Resultado: [bold green]CORRECTO[/bold green]")
console.print("[bold cyan]Textodestacado[/]")


