from pydantic import BaseModel
from app.schemas.role import RoleInfo
from app.schemas.permission import PermissionInfo

class RolePermimssionResponse(BaseModel):
    role_id: int
    permission_id: int
    role: RoleInfo
    permission: PermissionInfo