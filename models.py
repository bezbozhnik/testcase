from sqlalchemy  import Column, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
Base = declarative_base()
class Item(Base):
    __tablename__ = 'items'
    uuid = Column(String, primary_key=True)
    text = Column(String)

class ItemCreate(BaseModel):
    uuid: str
    text: str