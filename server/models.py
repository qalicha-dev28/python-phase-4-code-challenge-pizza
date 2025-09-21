from server.app import db

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    pizzas = db.relationship("RestaurantPizza", back_populates="restaurant", cascade="all, delete")

    def __repr__(self):
        return f"<Restaurant {self.name}>"

class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(250), nullable=False)

    restaurants = db.relationship("RestaurantPizza", back_populates="pizza", cascade="all, delete")

    def __repr__(self):
        return f"<Pizza {self.name}>"

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))

    restaurant = db.relationship("Restaurant", back_populates="pizzas")
    pizza = db.relationship("Pizza", back_populates="restaurants")

    def __repr__(self):
        return f"<RestaurantPizza {self.price}>"
