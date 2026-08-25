from pydantic import BaseModel
from app.schemas.role import RoleInfo
from app.schemas.user import UserResponse

class UserRoleResponse(BaseModel):
    user_id: int
    role_id: int
    role: RoleInfo
    user: UserResponse
    
class UserRoleInfo(UserRoleResponse):
    pass

class UserRoleCreate(UserRoleResponse):
    pass

class UserRoleUpdate(BaseModel):
    user_id: int | None = None
    role_id: int | None = None
    role: RoleInfo | None = None
    user: UserResponse | None = None