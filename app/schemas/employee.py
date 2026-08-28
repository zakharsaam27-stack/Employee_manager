from pydantic import BaseModel, ConfigDict
from app.schemas.user import UserResponse
from app.schemas.department import DepartmentInfo
from app.schemas.job_title_info import JobTitleInfo

class EmployeeCreate(BaseModel):
    full_name: str
    department_id: int
    job_title_id: int
    disabled: bool = False
    
class EmployeeResponse(BaseModel):
    id: int
    full_name: str
    user: UserResponse
    department: DepartmentInfo
    job_title: JobTitleInfo
    disabled: bool = False
    
    model_config = ConfigDict(from_attributes=True)
    
class EmployeeUpdate(BaseModel):
    full_name: str | None = None
    user: UserResponse | None = None
    department: DepartmentInfo | None = None
    job_title: JobTitleInfo | None = None
    disabled: bool | None = None
    
    model_config = ConfigDict(from_attributes=True)
