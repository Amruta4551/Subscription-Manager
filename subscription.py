from rich import print
from storage import add_subscription, get_all_subscriptions, find_subscription, delete_subscription

def create_subscription():
    name = input("Service Name: ")
    plan = input("Plan Type (Monthly/Yearly): ")
    cost = float(input("Cost: "))
    renewal = input("Renewal Date (DD-MM-YYYY): ")

    last_used = input("Last Used Date (DD-MM-YYYY): ")

    data = {
        "name": name,
        "plan": plan,
        "cost": cost,
        "renewal": renewal,
        "last_used": last_used,
        "status": "Active"
    }

    add_subscription(data)
    print("[bold white]Subscription added![/bold white]")

def read_subscriptions():
    return get_all_subscriptions()

def update_subscription():
    sub_id = int(input("Enter Subscription ID: "))
    sub = find_subscription(sub_id)

    if sub:
        sub["name"] = input("New Name: ")
        sub["plan"] = input("New Plan: ")
        sub["cost"] = float(input("New Cost: "))
        sub["renewal"] = input("New Renewal Date: ")
        sub["status"] = input("Status (Active/Cancelled): ")
        print("[bold white]Updated![/bold white]")
    else:
        print("Not found!")

def remove_subscription():
    sub_id = int(input("Enter ID to delete: "))
    delete_subscription(sub_id)
    print("[bold white]Deleted![/bold white]")
