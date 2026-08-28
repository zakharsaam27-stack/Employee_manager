from pydantic import BaseModel

class RoleInfo(BaseModel):
    id: int
    name: str