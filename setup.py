from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a database connection
engine = create_engine('sqlite:///data/restaurants.sqlite')

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()
