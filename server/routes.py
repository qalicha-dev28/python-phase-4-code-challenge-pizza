from flask import Blueprint, request, jsonify
from server.models import db, Pizza, Restaurant, RestaurantPizza

bp = Blueprint("api", __name__)

# Get all restaurants
@bp.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

# Get one restaurant with pizzas
@bp.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    data = restaurant.to_dict()
    data["pizzas"] = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    return jsonify(data)

# Delete restaurant
@bp.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return "", 204

# Get all pizzas
@bp.route("/pizzas", methods=["GET"])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas])

# Create restaurant-pizza association
@bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = data.get("price")
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")

        if price < 1 or price > 30:
            return jsonify({"errors": ["Price must be between 1 and 30."]}), 400

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        return jsonify(rp.pizza.to_dict()), 201
    except Exception:
        return jsonify({"errors": ["validation errors"]}), 400
