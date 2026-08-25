from pydantic import BaseModel
from app.schemas.employee import EmployeeResponse

class JobTitleInfo(BaseModel):
    id: int
    name: str
    
class JobTitleResponse(JobTitleInfo):
    employees: list[EmployeeResponse]
    
class JobTitleUpdate(BaseModel):
    name: str | None = None
    employees: list[EmployeeResponse]
    
class JobTitleCreate(BaseModel):
    name: str
    employess: list[EmployeeResponse]