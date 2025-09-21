from server.app import db, create_app
from server.models import Restaurant, Pizza, RestaurantPizza

def test_models():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()

        r = Restaurant(name="Test Place", address="123 Test Lane")
        p = Pizza(name="Test Pizza", ingredients="Cheese, Tomato")
        rp = RestaurantPizza(price=15, restaurant=r, pizza=p)

        db.session.add_all([r, p, rp])
        db.session.commit()

        assert r.id is not None
        assert p.id is not None
        assert rp.id is not None
        assert rp.restaurant.name == "Test Place"
        assert rp.pizza.name == "Test Pizza"

        db.drop_all()
