from db import engine
from sqlalchemy import inspect
from models import Item
# Проверяем наличие таблицы
inspector = inspect(engine)
if not inspector.has_table('items'):
    # Создаем таблицу
    Item.__table__.create(engine)