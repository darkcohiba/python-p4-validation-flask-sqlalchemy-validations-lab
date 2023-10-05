#!/usr/bin/env python3

from app import app
from models import db, Author, Post


if __name__ == '__main__':
    
    with app.app_context():
        # a1 = Author(name="Sky", phone_number= "3032711")
        # db.session.add(a1)
        # db.session.commit()
        # a2 = Author(name="Tri", phone_number= "3032234567")
        # db.session.add(a2)
        # db.session.commit()
        # names = [item[0] for item in db.session.query(Author.name).all()]
        # # names = db.session.query(Author.name).all()

        # print(names)
        # name = input("give me a name")
        # print(name)
        # if name in names:
        #     print("not unique")
        # else:
        #     print("unique")
        # import ipdb; ipdb.set_trace()
        
