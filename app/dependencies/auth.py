from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from app.db.session import get_session
from app.models import User
from app.core.security import decode_access_token, verify_password

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


