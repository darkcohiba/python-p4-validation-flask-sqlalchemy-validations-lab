#!/usr/bin/env python3

from app import app
from models import db, Author, Post

from faker import Faker

fake = Faker()



def create_author():
    authors = []
    for _ in range(50):
        u = Author(
            name = fake.name(), 
            phone_number = "9179996666",
        )
        authors.append(u)
    return authors

if __name__ == '__main__':
    
    with app.app_context():
        print("seedings authors")
        authors = create_author()
        db.session.add_all(authors)
        db.session.commit()
