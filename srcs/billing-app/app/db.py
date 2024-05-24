from sqlalchemy import insert
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import json
import orders

Session = sessionmaker(orders.engine)

def add_order(user_id, number_of_items, total_amount):
    sess = Session()
    sess.execute(insert(orders.orders).values(user_id=user_id, number_of_items=number_of_items, total_amount=total_amount))
    sess.commit()
    sess.close()

def process_order(body):
    data = json.loads(body)
    if 'user_id' in data and 'number_of_items' in data and 'total_amount' in data:
        try:
            uid = int(data['user_id'])
            number_of_items = int(data['number_of_items'])
            total_amount = int(data['total_amount'])
            print("-------Order added successfully----------")
            add_order(uid, number_of_items, total_amount)
        except ValueError as e:
            print("-------Adding order failed----------")
    else:
        print("-------Adding order failed----------")