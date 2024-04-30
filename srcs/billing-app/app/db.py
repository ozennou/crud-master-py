from sqlalchemy import insert, delete, update, select
from flask import jsonify
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import orders

Session = sessionmaker(orders.engine)

def add_order(user_id, number_of_items, total_amount):
    sess = Session()
    sess.execute(insert(orders.orders).values(user_id=user_id, number_of_items=number_of_items, total_amount=total_amount))
    sess.commit()
    sess.close()
