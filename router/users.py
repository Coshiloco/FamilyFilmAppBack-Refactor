from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer
from controllers.users import auth_user, create_token, validate_user,get_all_users,filter_user,create_userdata
from controllers.session import add_to_db
from schema.Group import LoginCreate
from schema.User import userCreate,userLogin,UserData
from models.User import User
from typing import List


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get('/all',response_model=List[UserData],status_code=200)
async def get_users():
    return [create_userdata(user_instance) for user_instance in get_all_users()]

@router.get('/{id:int}',response_model=UserData, status_code=200)
async def get_user(id:int):
        user_instance = filter_user('id',id)
        return create_userdata(user_instance)

oauth = OAuth2PasswordBearer(tokenUrl="/login")
@router.post('/login')
async def login_user(token: LoginCreate):
    print(token.token)
    user_validate = validate_user(token=token.token)
    return user_validate

@router.get('/me',status_code=200,response_model=UserData)
async def me(user = Depends(auth_user)):
    return create_userdata(user)