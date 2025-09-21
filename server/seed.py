from server.app import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    print("Seeding database...")

    # Clear tables
    db.drop_all()
    db.create_all()

    # Add restaurants
    r1 = Restaurant(name="Mario's Pizzeria", address="123 Pizza Street")
    r2 = Restaurant(name="Luigi's Pizza", address="456 Cheese Avenue")

    # Add pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie", ingredients="Tomato, Mozzarella, Peppers, Onions, Olives")

    # Add restaurant-pizza links
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=8, restaurant=r2, pizza=p3)

    db.session.add_all([r1, r2, p1, p2, p3, rp1, rp2, rp3])
    db.session.commit()

    print("✅ Database seeded!")
