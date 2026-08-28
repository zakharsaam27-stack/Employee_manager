from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, delete
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate

async def get_employee(
    asyncSession: AsyncSession,
    full_name: str | None = None,
    employeeId: int | None = None
):
    conditions = []
    
    if full_name is not None:
        conditions.append(Employee.full_name == full_name)
    if employeeId is not None:
        conditions.append(Employee.id == employeeId)
    if not conditions: 
        return None
    
    stmt = select(Employee).where(or_(*conditions))
    result = await asyncSession.execute(stmt)
    employee = result.scalars().all()
    
    return employee

async def create_employee(
    asyncSession: AsyncSession,
    data: EmployeeCreate
):
    employee = Employee(
        full_name=data.full_name,
        department_id=data.department_id,
        job_title_id=data.job_title_id
    )
    asyncSession.add(employee)
    await asyncSession.commit()
    await asyncSession.refresh(employee)
    
    return employee

async def update_employee(
    asyncSession: AsyncSession,
    data: EmployeeUpdate,
    employeeId: int
):
    stmt = select(Employee).where(Employee.id == employeeId)
    result = await asyncSession.execute(stmt)
    employee = result.scalar_one_or_none()
    
    if employee is None: 
        return None
    
    updates = data.model_dump(exclude_unset=True)
    
    for field, value in updates.items():
        setattr(employee, field, value)
    
    await asyncSession.commit()
    await asyncSession.refresh(employee)
    
    return employee


async def delete_employee(
    asyncSession: AsyncSession,
    employeeId: int
):
    stmt = delete(Employee).where(Employee.id == employeeId)
    await asyncSession.execute(stmt)
    await asyncSession.commit()