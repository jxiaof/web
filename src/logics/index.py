from typing import Optional
from models.model import Item

class Index():

    @staticmethod
    def say_hello():
        return {"Hello": "World"}

    @staticmethod
    def get_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

    @staticmethod
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}