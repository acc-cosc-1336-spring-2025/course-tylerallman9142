#

inventory = {}

def add_inventory(item_name: str, quantity: int):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_inventory_widget(item_name: str):
    if item_name in inventory:
        del inventory[item_name]
        return True
    return False