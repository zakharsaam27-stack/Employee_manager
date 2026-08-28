from pydantic import BaseModel, ConfigDict
from app.schemas.roleInfo import RoleInfo
from app.schemas.permission import PermissionInfo

class RolePermimssionResponse(BaseModel):
    role_id: int
    permission_id: int
    role: RoleInfo
    permission: PermissionInfo
    
    model_config = ConfigDict(from_attributes=True)
    
class RolePermissionInfo(RolePermimssionResponse):
    pass
    
class RolePermissionCreate(RolePermimssionResponse):
    pass

class RolePermissionUpdate(BaseModel):
    role_id: int | None = None
    permission_id: int | None = None
    role: RoleInfo | None = None
    permission: PermissionInfo | None = None
    
    model_config = ConfigDict(from_attributes=True)