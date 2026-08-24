from pydantic import BaseModel

class UserCreate(BaseModel):
  id: int
  email: str
  hashed_pass: str
  
  