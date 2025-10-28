from setup import session, Restaurant, Hotel
from sqlalchemy import or_

# Create instances of the Restaurant table class
nyc_diner = Restaurant(
    restaurant_name="NYC Diner",
    restaurant_city="New York City",
    famous_dish="Eggs Benedict"
)

metropolitan = Restaurant(
    restaurant_name="The Metropolitan",
    restaurant_city="London",
    famous_dish="Bangers and Mash"
)

chez_panisse = Restaurant(
    restaurant_name="Chez Panisse",
    restaurant_city="Berkeley",
    famous_dish="Duck a l'Orange"
)

bedford = Restaurant(
    restaurant_name="The Bedford",
    restaurant_city="Las Vegas",
    famous_dish="Martha's Oysters"
)

# Create instances of the Hotel table class
ritz = Hotel(hotel_name="The Ritz", hotel_city="Paris")
yuen_bettei_deita = Hotel(hotel_name="Yuen Bettei Deita", hotel_city="Tokyo")
casa_legado = Hotel(hotel_name="Casa Legado", hotel_city="Bogota")

create_data = [
    nyc_diner, metropolitan, chez_panisse, bedford, ritz, yuen_bettei_deita,
    casa_legado
]

# Since the session is already open, add a new restaurant record
# for data in create_data:
#     session.add(data)
# session.commit()

restaurants = session.query(Restaurant) \
    .order_by(Restaurant.restaurant_name.asc()) \
    .all()

for restaurant in restaurants:
    print(restaurant.restaurant_name, restaurant.restaurant_city)

restaurant = session.query(Restaurant) \
    .filter(Restaurant.restaurant_name == 'NYC Diner') \
    .one()

print(restaurant)

restaurants = session.query(Restaurant) \
    .filter(Restaurant.restaurant_city == 'Berkeley') \
    .all()

for restaurant in restaurants:
    print(restaurant.restaurant_name, restaurant.restaurant_city)

# Retrieve restaurants in city A or city B
restaurants = session.query(Restaurant) \
    .filter(or_(
        Restaurant.restaurant_city == 'London',
        Restaurant.restaurant_city == 'Las Vegas'
    )) \
    .all()

for restaurant in restaurants:
    print(restaurant.restaurant_name, restaurant.restaurant_city)
