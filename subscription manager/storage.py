subscriptions = []

def add_subscription(data):
    subscriptions.append(data)

def get_all_subscriptions():
    return subscriptions

def find_subscription(sub_id):
    for s in subscriptions:
        if str(s["id"]) == str(sub_id):
            return s
    return None

def delete_subscription(sub_id):
    global subscriptions
    subscriptions = [s for s in subscriptions if str(s["id"]) != str(sub_id)]