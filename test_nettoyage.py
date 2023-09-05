from nettoyage import is_available, purchase_product, multi_purchase_product, stock_report
import pytest


def test_avail():
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    assert is_available("apple", 20, inventory_test) == True
    assert is_available("apple", 60, inventory_test) == False
    assert is_available("grape", 10, inventory_test) == False


@pytest.mark.parametrize(
    "item_id,quantity,expected_result,expected_exception",
    [
        ("apple", 20, {"apple": 30, "banana": 25, "orange": 33}, None),
        ("banana", 50, {"apple": 50, "banana": 25, "orange": 33}, ValueError),
    ],
)
def test_purch(item_id, quantity, expected_result, expected_exception):
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    if expected_exception is not None:
        with pytest.raises(
            expected_exception,
            match="La commande est supérieure à la quantité en stock. Elle ne peut être validée",
        ):
            result = purchase_product(item_id, quantity, inventory_test)
            assert result == expected_result
    else:
        result = purchase_product(item_id, quantity, inventory_test)
        assert result == expected_result


@pytest.mark.parametrize(
    "orders,expected_responses",
    [
        (
            [("apple", 20), ("banana", 10), ("orange", 5), ("orange", 5)],
            {"apple": 30, "banana": 15, "orange": 23},
        ),
        (
            [("apple", 20), ("banana", 10), ("grape", 60)],
            {"apple": 30, "banana": 15, "orange": 33},
        ),
    ],
)
def test_multi_purch(orders, expected_responses):
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    assert multi_purchase_product(orders, inventory_test) == expected_responses


def test_report():
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    expected_report = "Stock Report:\nItem ID: apple, Quantity: 50\nItem ID: banana, Quantity: 25\nItem ID: orange, Quantity: 33\n"
    assert stock_report(inventory_test) == expected_report
