from pydantic import BaseModel,EmailStr
from typing import Optional, List

from schema import Movie,User

class GroupCreate(BaseModel):
    name:str

class LoginCreate(BaseModel):
    token:str
class AddUser(BaseModel):
    email:EmailStr

class GroupData(GroupCreate):
    id: int
    user_owner_id: int
    watchlist: Optional[List[Movie.movieData]] = []
    viewlist: Optional[List[Movie.movieData]] = []
    users: List[User.User]


class WatchListCreate(BaseModel):
    group_id:int
    movie_id:int

class ViewListCreate(WatchListCreate):
    pass