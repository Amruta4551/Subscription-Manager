import pandas as pd
from storage import get_all_subscriptions

def export_to_excel():
    data = get_all_subscriptions()

    if not data:
        print("No data to export!")
        return

    df = pd.DataFrame(data)
    df.to_excel("subscriptions.xlsx", index=False)

    print("Exported to subscriptions.xlsx")