from pydantic import BaseModel
from app.schemas.employee import EmployeeResponse

class DepartmentResponse(BaseModel):
    id: int
    name: str
    employees: list[EmployeeResponse]
    
class DepartmentInfo(BaseModel):
    id: int
    name: str
    
class DepartmentCreate(BaseModel):
    name: str
    employees: list[EmployeeResponse]
    
class DepartmentUpdate(BaseModel):
    name: str | None = None
    employees: list[EmployeeResponse] | None = None