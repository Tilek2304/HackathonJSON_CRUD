from cProfile import label
from settings import DB
import json
with open(DB) as db:
    bd_list = json.load(db)
    for i in bd_list:
        print(i.get('price'))
    # bd_list.sort(key=lambda x: int(x.get('id')))
    # print(bd_list)