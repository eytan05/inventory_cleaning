from typing import Dict, List, Tuple


def get_inventory() -> Dict[str, int]:
    inventory = {"apple": 50, "banana": 25, "orange": 33}
    return inventory


def is_available(item_id: str, quantity: int, inventory_db: Dict[str, int]) -> bool:
    return item_id in inventory_db and inventory_db[item_id] >= quantity


def purchase_product(item_id: str, quantity: int, inventory_db: Dict[str, int]) -> Dict[str, int]:
    if is_available(item_id, quantity, inventory_db):
        inventory_db[item_id] -= quantity
    else:
        raise ValueError(
            "La commande est supérieure à la quantité en stock. Elle ne peut être validée"
        )
    return inventory_db


def multi_purchase_product(
    order_list: List[Tuple[str, int]], inventory_db: Dict[str, int]
) -> Dict[str, int]:
    for item_id, quantity in order_list:
        if is_available(item_id, quantity, inventory_db):
            inventory_db[item_id] -= quantity
    return inventory_db


def stock_report(inv: Dict[str, int]) -> str:
    report_str = "Stock Report:\n"
    for k, v in inv.items():
        report_str += f"Item ID: {k}, Quantity: {v}\n"
    return report_str
