import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class User (Base):
    id = Column(Integer, primary_key = True)
    username = Column(String(30), nullable = False)
    password = Column(String(30), nullable = False)
    email = Column(String, nullable = True)
    def serialize(self):
        return {
            'username': self.username,
            'email': self.email
            
        }
    
class Planet (Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    population = Column(Integer, nullable = False)
    def serialize(self):
        return {
            'name': self.name,
            'population': self.population
        }

class Character (Base):
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    age = Column(Integer, nullable = False)
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age
        }
    
class Vehicle (Base):
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    top_speed = Column(Integer, nullable = False)
    def serialize(self):
        return {
            'name': self.name,
            'top_speed': self.top_speed
        }
    
class FavoriteList (Base):
    __tablename__ = 'favorite list'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    planet = relationship(Planet)
    character = relationship(Character)
    vehicle = relationship(Vehicle)
    def serialize(self):
        return {
            
        }

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
