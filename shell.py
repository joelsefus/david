#!/usr/bin/env python
import os
import sys

import transaction
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from trumpet.models.base import Base, DBSession

from david.models.main import Address, Contact, Location
from david.models.main import Client, ClientContact

dburl = 'sqlite:///%s/david.sqlite' % os.getcwd()

settings = {'sqlalchemy.url' : dburl}
engine = engine_from_config(settings)
DBSession.configure(bind=engine)
Base.metadata.bind = engine
Base.metadata.create_all(engine)


s = DBSession()

