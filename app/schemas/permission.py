from pydantic import BaseModel

class PermissionInfo(BaseModel):
    id: int
    action: str
    