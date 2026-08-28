from fastapi import Depends, APIRouter
from app.db.session import get_session
from app.services.employee import get_employee, create_employee, update_employee, delete_employee
from app.dependencies import get_current_admin_user
from app.schemas import EmployeeResponse, EmployeeCreate, EmployeeUpdate

router = APIRouter(
    prefix="/admin/employees",
    tags=["Admin Employees"],
    dependencies=[Depends(get_current_admin_user)]
)


@router.get("/get-employee/{queue}", response_model=EmployeeResponse)
async def getEmployee(
    asyncSession = Depends(get_session),
    full_name: str | None = None,
    employeeId: int | None = None,
):
    return await get_employee(asyncSession, full_name, employeeId)


@router.post("/create-employee", response_model=EmployeeResponse)
async def createEmployee(
    data: EmployeeCreate,
    asyncSession = Depends(get_session),
):
    return await create_employee(asyncSession, data)

@router.patch("/update-employee", response_model=EmployeeResponse)
async def updateEmployee(
    data: EmployeeUpdate,
    employeeId: int,
    asyncSession = Depends(get_session),
):
    return await update_employee(asyncSession, data, employeeId)
    
    
@router.delete("/delete-employee")
async def deleteEmployee(
    employeeId: int,
    asyncSession = Depends(get_session),
):
    await delete_employee(asyncSession, employeeId)
    