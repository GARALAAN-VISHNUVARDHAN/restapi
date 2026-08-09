from sqlalchemy import Integer,String,Float,Column,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Relationship
base=declarative_base()
class users(base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String,unique=True)
    age=Column(Integer)
    password=Column(String)

    oder=Relationship("Oders",back_populates="user")

class Oders(base):
    __tablename__="Oders"
    id=Column(Integer,index=True,primary_key=True)
    pname=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))
    user=Relationship("users",back_populates="oder")
