from pydantic import BaseModel, ConfigDict
from app.schemas.employee import EmployeeResponse

class JobTitleResponse(BaseModel):
    id: int
    name: str
    employees: list[EmployeeResponse]
    
    model_config = ConfigDict(from_attributes=True)
    
class JobTitleUpdate(BaseModel):
    name: str | None = None
    employees: list[EmployeeResponse]
    
    model_config = ConfigDict(from_attributes=True)
    
class JobTitleCreate(BaseModel):
    name: str
    employess: list[EmployeeResponse]
    
    model_config = ConfigDict(from_attributes=True)