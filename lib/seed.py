#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie
from faker import Faker

# Replace 'sqlite:///your_database.db' with your actual database URL
DATABASE_URL = 'sqlite:///freebies.db'
engine = create_engine(DATABASE_URL)

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create Faker instance
fake = Faker()

# Populate Companies
for _ in range(5):  # Create 5 companies
    company = Company(name=fake.company(), founding_year=fake.year())
    session.add(company)

# Populate Devs
for _ in range(10):  # Create 10 devs
    dev = Dev(name=fake.name())
    session.add(dev)

# Populate Freebies
for _ in range(20):  # Create 20 freebies
    freebie = Freebie(
        item_name=fake.word(),
        value=fake.random_int(min=1, max=100),
        company_id=fake.random_int(min=1, max=5),  # Assuming 5 companies were created
        dev_id=fake.random_int(min=1, max=10),  # Assuming 10 devs were created
    )
    session.add(freebie)

# Commit the changes
session.commit()

# Close the session
session.close()

