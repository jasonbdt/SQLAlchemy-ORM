from typing import Self
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a database connection
engine = create_engine('sqlite:///data/restaurants.sqlite')

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()

# Define the data table class's parent class
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    restaurant_id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_name = Column(String)
    restaurant_city = Column(String)
    famous_dish = Column(String)

    def __repr__(self: Self) -> str:
        return f"Restaurant(restaurant_id = {self.restaurant_id}, "\
               f"name = {self.restaurant_name})"


class Hotel(Base):
    __tablename__ = 'hotels'

    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_name = Column(String)
    hotel_city = Column(String)

    def __repr__(self: Self) -> str:
        return f"Hotel(hotel_id = {self.hotel_id}, "\
               f"name = {self.hotel_name})"


Base.metadata.create_all(engine)

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
for data in create_data:
    session.add(data)
session.commit()
