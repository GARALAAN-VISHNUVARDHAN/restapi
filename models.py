from pydantic import BaseModel,ConfigDict
class users(BaseModel):
    id:int
    name:str
    email:str
    age:int
    password:str
class oderresponse(BaseModel):
    id:int
    pname:str
    user_id:int
    model_config=ConfigDict(from_attributes=True)
class usersresponse(BaseModel):
    id:int
    name:str
    email:str
    age:int
    oder:list[oderresponse]
    model_config=ConfigDict(from_attributes=True)
class oders(BaseModel):
    id:int
    pname:str
    user_id:int

