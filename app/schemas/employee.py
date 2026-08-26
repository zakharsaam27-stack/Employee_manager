from pydantic import BaseModel
from app.schemas.user import UserResponse
from app.schemas.department import DepartmentInfo
from app.schemas.job_title import JobTitleInfo

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

class EmployeeInfo(EmployeeResponse):
    pass
    
class EmployeeUpdate(BaseModel):
    full_name: str | None = None
    user: UserResponse | None = None
    department: DepartmentInfo | None = None
    job_title: JobTitleInfo | None = None
    disabled: bool | None = None
