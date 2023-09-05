from flask import Flask, request, jsonify
from nettoyage import is_available, purchase_product, multi_purchase_product, stock_report, get_inventory

app = Flask(__name__)


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(get_inventory())


@app.route("/availability/<item_id>/<int:quantity>", methods=["GET"])
def check_availability(item_id, quantity):
    inventory_db = get_inventory()
    return jsonify(is_available(item_id, quantity, inventory_db))


@app.route("/purchase", methods=["POST"])
def purchase_item():
    item_id = request.json["item_id"]
    quantity = request.json["quantity"]
    inventory_db = get_inventory()
    try:
        updated_inventory = purchase_product(item_id, quantity, inventory_db)
        return jsonify(updated_inventory)
    except ValueError as e:
        return str(e), 400


@app.route("/multi_purchase", methods=["POST"])
def multi_purchase_items():
    order_list = request.json["order_list"]
    inventory_db = get_inventory()
    updated_inventory = multi_purchase_product(order_list, inventory_db)
    return jsonify(updated_inventory)


@app.route("/report", methods=["GET"])
def get_report():
    inventory_db = get_inventory()
    return stock_report(inventory_db)


if __name__ == "__main__":
    app.run(debug=True)
