from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

from subscription import create_subscription, read_subscriptions, update_subscription, remove_subscription
from export_excel import export_to_excel

console = Console()

def show_menu():
    console.print(Panel.fit(
        "[bold cyan]Subscription Manager[/bold cyan]\n\n"
        "1. Add Subscription\n"
        "2. View Subscriptions\n"
        "3. Update Subscription\n"
        "4. Delete Subscription\n"
        "5. Export to Excel\n"
        "6. Smart Suggestion\n"
        "7. Show Total Expense\n"
        "8. Exit",
        title="MENU",
        border_style="bold yellow"
    ))

def display_subscriptions():
    subs = read_subscriptions()

    if not subs:
        console.print("[bright_red]No data![/bright_red]")
        return

    table = Table(title="[bold]Subscriptions[/bold]")

    table.add_column("ID", style="cyan")
    table.add_column("Name")
    table.add_column("Plan")
    table.add_column("Cost")
    table.add_column("Renewal")
    table.add_column("Status")

    for s in subs:
        table.add_row(
            str(s["id"]),
            s["name"],
            s["plan"],
            str(s["cost"]),
            s["renewal"],
            s["status"]
        )

    console.print(table)

def suggestions():
    subs = read_subscriptions()
    today = datetime.today()

    console.print("\n[bold blue]Smart Suggestions:[/bold blue]")

    for s in subs:
        renewal_date = datetime.strptime(s["renewal"], "%d-%m-%Y")
        last_used = datetime.strptime(s["last_used"], "%d-%m-%Y")

        days_left = (renewal_date - today).days
        days_unused = (today - last_used).days

        # Expired
        if days_left < 0:
            console.print(f"[red] {s['name']} is expired! Renew or remove it.[/red]")

        # Expiring soon
        elif days_left <= 2:
            console.print(f"[yellow] {s['name']} will expire in {days_left} days[/yellow]")

        # Not used recently
        if days_unused > 15:
            console.print(f"[magenta] You haven’t used {s['name']} for {days_unused} days. Consider cancelling.[/magenta]")

        # Expensive subscription
        if s["cost"] > 500:
            console.print(f"[cyan] {s['name']} is costly (₹{s['cost']}). Consider basic plan.[/cyan]")

def total_expense():
    subs = read_subscriptions()
    total = sum(s["cost"] for s in subs if s["status"] == "Active")
    console.print(f"[bold yellow]Total Expense: ₹{total}[/bold yellow]")

def main():
    while True:
        show_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            create_subscription()
        elif choice == "2":
            display_subscriptions()
        elif choice == "3":
            update_subscription()
        elif choice == "4":
            remove_subscription()
        elif choice == "5":
            export_to_excel()
        elif choice == "6":
            suggestions()
        elif choice == "7":
            total_expense()
        elif choice == "8":
            console.print("[red]Exiting...[/red]")
            break
        else:
            console.print("[red]Invalid choice![/red]")

if __name__ == "__main__":
    main()