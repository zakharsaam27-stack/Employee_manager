from pydantic import BaseModel, ConfigDict
from app.schemas.role_permission import RolePermimssionResponse
from app.schemas.user_role import UserRoleResponse
    
class RoleResponse(BaseModel):
    id: int
    name: str
    user_roles: list[UserRoleResponse]
    
    model_config = ConfigDict(from_attributes=True)
    
class RoleUpdate(BaseModel):
    name: str | None = None
    role_permission: list[RolePermimssionResponse] | None = None
    
    model_config = ConfigDict(from_attributes=True)
    
class RoleCreate(BaseModel):
    name: str
    role_permission: list[RolePermimssionResponse]
    
    model_config = ConfigDict(from_attributes=True)