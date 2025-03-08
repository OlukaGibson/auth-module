from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    created_at: str
    applications: List['Application'] = []

    class Config:
        orm_mode = True

class Application(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_at: str
    users: List[User] = []
    roles: List['Role'] = []

    class Config:
        orm_mode = True

class Role(BaseModel):
    id: int
    name: str
    description: Optional[str]
    application_id: int
    application: Application
    users: List['UserRole'] = []

    class Config:
        orm_mode = True

class UserRole(BaseModel):
    id: int
    user_id: int
    role_id: int
    application_id: int
    user: User

    class Config:
        orm_mode = True