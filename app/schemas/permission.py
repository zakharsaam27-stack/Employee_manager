from pydantic import BaseModel

class PermissionInfo(BaseModel):
    id: int
    action: str
    
class PermissionResponse(PermissionInfo):
    pass
    
class PermissionCreate(BaseModel):
    action: str
    
class PermissinoUpdate(BaseModel):
    action: str | None = None