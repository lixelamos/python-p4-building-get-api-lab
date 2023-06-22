#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Bakery, BakedGood

fake = Faker()

with app.app_context():
    b = Bakery.query.filter_by(name="Mr. Bakery").first()
    if b:
        db.session.delete(b)
        db.session.commit()

...

with app.app_context():
    bg = BakedGood.query.filter_by(name="Madeleine").first()
    if bg:
        db.session.delete(bg)
        db.session.commit()
