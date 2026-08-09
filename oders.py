from fastapi import APIRouter,Depends

from models import oders,oderresponse
from sqlalchemy.orm import Session
import database_models
from database import get_db
router=APIRouter()

# @router.get("/")
# async def home():
#     return "new working perfectly"
@router.post("/",response_model=oderresponse)
async def create(oder:oders,db:Session=Depends(get_db)):
    o=database_models.Oders(id=oder.id,
           pname=oder.pname,user_id=oder.user_id

           )
    db.add(o)
    db.commit()
    return o
@router.get("/")
async def odersdeitals(db:Session=Depends(get_db)):
    d=db.query(database_models.Oders).all()
    return d



