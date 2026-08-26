from app.core.config import settings
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

def hash_password(password: str):
    hashed_pass = pwd_context.hash(password)
    return hash_password

def verify_password(password: str, hashed_pass: str):
    result = pwd_context.verify(password, hashed_pass)
    return result

def create_access_token(userId: int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode = {
        "sub": userId,
        "exp": expire
    }
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, [ALGORITHM])
    except JWTError as err:
        print(err)
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)