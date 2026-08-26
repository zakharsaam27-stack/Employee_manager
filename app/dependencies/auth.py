from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from app.models import User, Employee
from app.core.security import decode_access_token
from app.services import get_user_roles

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def get_current_user(
    asyncSession: AsyncSession,
    token: str = Depends(oauth2_scheme),
):  
    payload = decode_access_token(token)
    userId = payload.get("sub")
    
    result = await asyncSession.execute(
        select(User).where(User.id == userId)
    )
    user = result.scalar_one_or_none()
    
    if user is None:
        return None
    
    return user


async def get_current_active_user(
    user: User = Depends(get_current_user)
):
    if user.disabled:
        return None
    if user is None:
        return None
    else:
        return user


async def get_current_employee(
    asyncSession: AsyncSession,
    current_active_user = Depends(get_current_active_user)
):
    stmt = (
        select(Employee)
        .join(Employee.user)
        .where(current_active_user.id == User.id)
    )
    result = await asyncSession.execute(stmt)
    employee = result.scalar_one_or_none()
    
    return employee


async def get_current_admin_user(
    asyncSession: AsyncSession,
    current_active_user = Depends(get_current_active_user),
):
    user_roles = await get_user_roles(
        asyncSession, current_active_user.id
    )
    if any(role.role.name == "admin" for role in user_roles):
        return current_active_user
    
    raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
