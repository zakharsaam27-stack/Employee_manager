from pydantic import BaseModel
from app.schemas.role import RoleInfo
from app.schemas.user import UserResponse

class UserRoleResponse(BaseModel):
    user_id: int
    role_id: int
    role: RoleInfo
    user: UserResponse