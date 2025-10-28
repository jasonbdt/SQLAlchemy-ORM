from setup import session, Restaurant


restaurant_to_update = session.query(Restaurant) \
    .filter(Restaurant.restaurant_name == "NYC Diner") \
    .one()

restaurant_to_update.famous_dish = "French Toast and Bacon"
session.commit()

metropolitan = session.query(Restaurant) \
    .filter(Restaurant.restaurant_name == "The Metropolitan") \
    .one()

metropolitan.restaurant_city = "Luxembourg"
session.commit()
