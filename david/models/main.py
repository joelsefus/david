from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode, UnicodeText
from sqlalchemy import ForeignKey, Boolean
from sqlalchemy import Date, Time, DateTime
from sqlalchemy import Enum
from sqlalchemy import PickleType


from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import relationship, backref

from trumpet.models.base import Base

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(Unicode(150))
    street2 = Column(Unicode(150), default=None)
    city = Column(Unicode(50))
    state = Column(Unicode(2))
    zip = Column(Unicode(10))
    
class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    firstname = Column(Unicode(50))
    lastname = Column(Unicode(50))
    email = Column(Unicode(50), unique=True)
    phone = Column(Unicode(20))
    
    def __init__(self, firstname='', lastname='', email='', phone=''):
        if firstname:
            self.firstname = firstname
        if lastname:
            self.lastname = lastname
        if email:
            self.email = email
        if phone:
            self.phone = phone
            
class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), unique=True)
    address_id = Column(Integer, ForeignKey('addresses.id'))
    
    def __init__(self, name):
        self.name = name
        
class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), unique=True)
    address_id = Column(Integer, ForeignKey('addresses.id'))
    
    def __init__(self, name):
        self.name = name
        
class ClientContact(Base):
    __tablename__ = 'client_contacts'
    client_id = Column(Integer, ForeignKey('clients.id'), primary_key=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'), primary_key=True)

    def __init__(self, client_id, contact_id):
        self.client_id = client_id
        self.contact_id = contact_id



        
