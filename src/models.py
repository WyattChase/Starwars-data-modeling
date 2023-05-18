import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    

class UserFavorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))



class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Pyt
    # hon instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hairColor = Column(String(250), nullable=True)
    eyeColor = Column(String(250), nullable=True)
    skinColor = Column(String(250), nullable=True)
    Gender = Column(String(250), nullable=True)
    birthYear = Column(String(250), nullable=True)
    homeWorld = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    description = Column(String(250), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))



class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Integer, nullable=True)
    crew = Column(Integer, nullable=True)
    passengers = Column(Integer, nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    vehicle_class = Column(String(255), nullable=True)


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Integer, nullable=True)
    crew = Column(Integer, nullable=True)
    passengers = Column(Integer, nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    hyperdrive_rating = Column(Integer, nullable=True)


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')