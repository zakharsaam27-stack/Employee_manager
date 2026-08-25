from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    email: str | None = None
    hashed_pass: str | None = None
    
class UserResponse(BaseModel):
    id: int
    email: str
    
class UserInfo(UserResponse):
    pass
    
