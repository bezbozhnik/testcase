from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine(
    'postgresql://postgres:123@db/example', # Ваши настройки postgres`а
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)