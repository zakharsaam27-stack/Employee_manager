from pydantic import BaseModel, ConfigDict
from app.schemas.roleInfo import RoleInfo
from app.schemas.user import UserResponse

class UserRoleResponse(BaseModel):
    user_id: int
    role_id: int
    role: RoleInfo
    user: UserResponse
    
    model_config = ConfigDict(from_attributes=True)
    
class UserRoleInfo(UserRoleResponse):
    pass

class UserRoleCreate(UserRoleResponse):
    pass

class UserRoleUpdate(BaseModel):
    user_id: int | None = None
    role_id: int | None = None
    role: RoleInfo | None = None
    user: UserResponse | None = None
    
    model_config = ConfigDict(from_attributes=True)