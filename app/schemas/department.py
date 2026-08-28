from pydantic import BaseModel, ConfigDict
from app.schemas.employeeInfo import EmployeeInfo

class DepartmentResponse(BaseModel):
    id: int
    name: str
    employees: list[EmployeeInfo]
    
    model_config = ConfigDict(from_attributes=True)
    
class DepartmentInfo(BaseModel):
    id: int
    name: str
    
class DepartmentCreate(BaseModel):
    name: str
    
class DepartmentUpdate(BaseModel):
    name: str | None = None