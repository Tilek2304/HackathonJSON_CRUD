from os import system
from settings import DB
import json
from datetime import datetime

    # {
    #     "id": "1",
    #     "title": "name1",
    #     "price": "1",
    #     "created_date": "1",
    #     "updated_date": "1",
    #     "description": "some text",
    #     "status": "1"
    # },

def get_data(filter_='price', page=0, fprice=1000000, fbool=True, created_date=None):
    with open(DB) as db:
        if filter_ == 'price':
            bd_list = json.load(db)
            for i in sorted(bd_list, key=lambda x: x.get('price')):
                id_ = i.get('id')
                title = i.get('title')
                price = int(i.get('price'))
                status = i.get('status')
                if price<fprice and fbool==True or price>fprice and fbool==False:
                    print('------------------------------------------------')
                    print(f'id: {id_} | title: {title} | price: {price} | status: {status}')
                    print('------------------------------------------------')
                # if page == 0:
                    
        elif filter_ == 'status':
            bd_list = json.load(db)
            for i in sorted(bd_list, key=lambda x: x.get('status')):
                id_ = i.get('id')
                title = i.get('title')
                price = i.get('price')
                status = i.get('status')
                if status=='продано' and fbool==True or status=='не продано' and fbool==False:
                    print('------------------------------------------------')
                    print(f'id: {id_} | title: {title} | price: {price} | status: {status}')
                    print('------------------------------------------------')
                # if page == 0:
        elif filter_ == 'created_date':
            bd_list = json.load(db)
            for i in bd_list:
                id_ = i.get('id')
                title = i.get('title')
                price = i.get('price')
                status = i.get('status')
                if created_date==i.get('created_date'):
                    print('------------------------------------------------')
                    print(f'id: {id_} | title: {title} | price: {price} | status: {status}')
                    print('------------------------------------------------')
                # if page == 0:

def create():
    data = {
        'id': datetime.now().strftime('%H%M%S'),
        'title': input('Введите название: '),
        'price': input('Введите цену: '),
        'created_date': str(datetime.now().strftime('%d.%m.%Y %H:%M')),
        'updated_date': str(datetime.now().strftime('%d.%m.%Y %H:%M')),
        'description': input('Введите описание: '),
        'status': input('Введите статус продано/не продано: ')
    }
    with open(DB) as db:
        json_data: list = json.load(db)
        json_data.append(data)
    with open(DB, 'w') as db:
        json.dump(json_data, db, indent=4)


def get_by_id():
    with open(DB) as db:
        id_ = input('Введите ID: ')
        for i in json.load(db):
            if i.get('id') == id_:
                title = i.get('title')
                price = i.get('price')
                status = i.get('status')
                created_date = i.get('created_date')
                updated_date = i.get('updated_date')
                description = i.get('description')
                print(f'title: {title}')
                print(f'price: {price}')
                print(f'created date: {created_date}')
                print(f'updated date: {updated_date}')
                print(f'description: {description}')
                print(f'status: {status}')
                return None
        print('Такого ID нет!!!')

# get_data(filter_='created_date', created_date='26.08.2022 19:42')

def update():
    with open(DB) as db:
        id_ = input('Введите ID: ')
        data: list = json.load(db)
        for obj in data:
            if obj['id'] == id_:
                obj['title'] = input('Введите название: ') or obj['title']
                obj['price'] = input('Введите цену') or obj['price']
                obj['status'] = input('Введите статус продано/не продано: ') or obj['status']
                obj['created_date'] = obj['created_date']
                obj['updated_date'] = str(datetime.now().strftime('%d.%m.%Y %H:%M'))
                obj['description'] = input('Введите описание: ') or obj['description']
                with open(DB, 'w+') as db:
                    json.dump(data, db, indent=4)
                return None
        print('Такого ID нет')

def delete_data():
    with open(DB) as db:
        id_ = input('Введите ID: ')
        data: list = json.load(db)
        for obj in data:
            if obj['id'] == id_:
                data.remove(obj)
                with open(DB, 'w') as db:
                    json.dump(data, db, indent=4)
                return []
        print('Такого ID нет')
get_data()
get_by_id()
update()
get_data()
create()
get_data()
delete_data()
get_data()