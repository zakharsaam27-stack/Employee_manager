from fastapi import Depends, HTTPException, status, APIRouter
from app.db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.employee import get_employee

router = APIRouter(
    prefix="/admin/employees",
    tags=["Admin Employees"]
)

