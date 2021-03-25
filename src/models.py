import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False) 
    second_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(250),  nullable=False)
    fav_characters = relationship("Favorites_Characters")
    fav_vehicles = relationship("Favorites_Vehicles")
    fav_planets = relationship("Favorites_Planets")

class Characters(Base):
    __tablename__ = "characters"
    uid = Column(Integer, primary_key=True)
    name = Column(String(20))
    height = Column(Float)
    mass = Column(Float)
    hair_color = Column(String(20)) 
    skin_color = Column(String(20)) 
    eye_color = Column(String(20)) 
    birth_year = Column(Date) 
    gender = Column(String(20)) 
    created = Column(Date) 
    edited = Column(Date) 
    homeworld = Column(String(20))
    liked_by_users = relationship("Favorites_Characters")

class Planet(Base):
    __tablename__ = "planet"
    uid = Column(Integer, primary_key=True)
    name = Column(String(20)) 
    diameter = Column(Float)
    rotation_period = Column(Float)
    orbital_period = Column(Float)
    gravity = Column(Float)
    population = Column(Integer)
    climate = Column(String(20)) 
    terrain = Column(String(20)) 
    surface_water = Column(Integer)
    created = Column(Date)
    edited = Column(Date)
    liked_by_users = relationship("Favorites_Planets")

class Vehicle(Base):
    __tablename__ = "vehicle"
    uid = Column(Integer, primary_key=True)
    name = Column(String(20)) 
    model = Column(String(20)) 
    starship_class = Column(String(20)) 
    manufacturer = Column(String(20)) 
    cost_in_credits = Column(Integer) 
    length = Column(Float) 
    crew = Column(Float) 
    passengers = Column(Integer) 
    max_atmosphering_speed = Column(Float) 
    hyperdrive_rating = Column(Float) 
    mglt = Column(Integer) 
    cargo_capacity = Column(Integer) 
    consumables = Column(String(20)) 
    pilots = Column(Integer) 
    created = Column(Date)
    edited = Column(Date)
    liked_by_users = relationship("Favorites_Vehicles")

class Favorites_Characters(Base):
    __tablename__ = "favorites_characters"
    uid = Column(Integer, primary_key=True)
    user_uid = Column(Integer, ForeignKey('user.uid'))
    character_uid = Column(Integer, ForeignKey('characters.uid'))

class Favorites_Vehicles(Base):
    __tablename__ = "favorites_vehicles"
    uid = Column(Integer, primary_key=True)
    user_uid  = Column(Integer, ForeignKey('user.uid'))
    vehicle_uid = Column(Integer, ForeignKey('vehicle.uid'))

class Favorites_Planets(Base):
    __tablename__ = "favorites_planets"
    uid = Column(Integer, primary_key=True)
    user_uid  = Column(Integer, ForeignKey('user.uid'))
    planet_uid = Column(Integer, ForeignKey('planet.uid'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')