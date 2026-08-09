from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# db_url="postgresql://postgres:newpassword@localhost:5432/shop_db"
db_url = "postgresql://postgres:newpassword@db:5432/shop_db"
engine=create_engine(db_url)
session=sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()