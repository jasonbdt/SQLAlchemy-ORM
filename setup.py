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

# Create an instance of the Restaurant table class
restaurant = Restaurant(
    restaurant_name="NYC Diner",
    restaurant_city="New York City",
    famous_dish="Eggs Benedict"
)

# Since the session is already open, add a new restaurant record
session.add(restaurant)
session.commit()
