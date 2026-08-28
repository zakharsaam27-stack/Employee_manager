from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone
from passlib.context import CryptContext
from app.routers import admin_employee

app = FastAPI()

app.include_router(admin_employee.router)