from fastapi import FastAPI, HTTPException
from db import SessionLocal
from models import Item, ItemCreate
app = FastAPI()

# Эндпоинт для сохранения записи
@app.post("/new")
def create_item(items: list[ItemCreate]):
    db = SessionLocal()
    response = []
    for item in items:
        db_item = Item(uuid=item.uuid, text=item.text)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        response.append({"uuid": db_item.uuid, "text": db_item.text})
    db.close()
    return response

# Эндпоинт для получения всех записей
@app.get("/all")
def get_all_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

# Эндпоинт для получения конкретной записи
@app.get("/{uuid}")
def get_item(uuid: str):
    if uuid.isdigit():
        # Обработка целочисленного значения
        return get_items(uuid)
    db = SessionLocal()
    item = db.query(Item).filter(Item.uuid == uuid).first()
    db.close()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Эндпоинт для получения указанного количества записей
@app.get("/{count}")
def get_items(count: int):
    db = SessionLocal()
    items = db.query(Item).limit(count).all()
    db.close()
    return items

# Эндпоинт для удаления записи
@app.delete("/{uuid}")
def delete_item(uuid: str):
    db = SessionLocal()
    item = db.query(Item).filter(Item.uuid == uuid).first()
    if not item:
        db.close()
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    db.close()
    return {"message": "Item deleted"}