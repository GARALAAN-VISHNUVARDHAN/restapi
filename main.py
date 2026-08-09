from fastapi import FastAPI,Depends,HTTPException
from database import engine
from database import get_db
import database_models 
from sqlalchemy.orm import Session
from models import users,usersresponse
import oders
from password import ph
database_models.base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(oders.router,prefix="/oders",tags=["new tags"])



@app.get("/")
async def home():
    return "url routing workign correctly"
@app.post("/register",response_model=usersresponse)
async def resgister(user:users,db:Session=Depends(get_db)):
    hashpass=ph.hash(user.password)
    f=(db.query(database_models.users).filter(database_models.users.email==user.email).first())
    if f:
        raise HTTPException(status_code=409,detail="user alredy exits")
    new_user=database_models.users(id=user.id,name=user.name,age=user.age,email=user.email,password=hashpass)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except Exception as e:
        db.rollback()
        print("DATABASE ERROR:", e)

        raise HTTPException(
            status_code=500,
            detail="Registration failed"
        )
@app.get("/users",response_model=list[usersresponse])
async def get_detials(db:Session=Depends(get_db)):
    users_d=db.query(database_models.users).all()
    return users_d

@app.post("/users")
async def insert(users:users,db:Session=Depends(get_db)):
    db.add(database_models.users(**users.model_dump()))
    db.commit()
    return users
@app.get("/users{id}")
async def find(id:int,db:Session=Depends(get_db)):
    f=db.query(database_models.users).filter(database_models.users.id==id).first()
    if f:
        return f
    else:
        return f'with this id:{id} we dont find data'
@app.delete("/users")
async def delete(id:int,db:Session=Depends(get_db)):
    f=db.query(database_models.users).filter(database_models.users.id==id).first()
    if f:
        db.delete(f)
        db.commit()
        return "deleted"
    else:
        return "we dont find the data"

@app.put("/users")
async def update(id:int,user:users,db:Session=Depends(get_db)):
    f=db.query(database_models.users).filter(database_models.users.id==id).first()
    if f:
        f.age=user.age
        f.email=user.email
        f.name=user.name
        db.commit()
        
        
    else:
        raise HTTPException(status_code=404,detail="item not found")
        
        