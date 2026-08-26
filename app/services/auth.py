from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import User
from app.core.security import verify_password

async def authenticate_user(
    email: str,
    password: str,
    asyncSession: AsyncSession
):
    result = await asyncSession.execute(
        select(User)
        .where(User.email == email)
    )
    data = result.scalar_one_or_none()
    if data is None:
        return None
    pass_check = verify_password(password, data.hashed_pass)
    if pass_check:
        return data
    return None