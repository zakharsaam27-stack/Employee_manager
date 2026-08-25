from pydantic import BaseModel
from app.schemas.role_permission import RolePermimssionResponse
from app.schemas.user_role import UserRoleResponse

class RoleInfo(BaseModel):
    id: int
    name: str
    role_permission = list[RolePermimssionResponse]
    
class RoleResponse(RoleInfo):
    user_roles: list[UserRoleResponse]
    
class RoleUpdate(BaseModel):
    name: str | None = None
    role_permission: list[RolePermimssionResponse] | None = None
    
class RoleCreate(BaseModel):
    name: str
    role_permission: list[RolePermimssionResponse]