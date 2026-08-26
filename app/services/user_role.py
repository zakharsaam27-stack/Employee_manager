from app.models import User_role
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_user_roles(
    asyncSession: AsyncSession,
    userId: str
):
    result = await asyncSession.execute(
        select(User_role)
        .where(User_role.user_id == userId)
    )
    user_role = result.scalars().all()
    return user_role