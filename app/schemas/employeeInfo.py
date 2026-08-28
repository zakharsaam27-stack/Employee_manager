from pydantic import BaseModel, ConfigDict
from app.schemas.job_title_info import JobTitleInfo
from app.schemas.user import UserResponse

class EmployeeInfo(BaseModel):
    id: int
    full_name: str
    user: UserResponse
    job_title: JobTitleInfo
    disabled: bool = False
    
    model_config = ConfigDict(from_attributes=True)