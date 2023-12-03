# routers.py
from fastapi import APIRouter, Depends, status, Header
from sqlalchemy.orm import Session
from app.services.auth import login, get_refresh_token
from app.db.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/login", status_code=status.HTTP_200_OK)
async def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await login(user_credentials, db)


@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh_access_token(refresh_token: str = Header(), db: Session = Depends(get_db)):
    return await get_refresh_token(token=refresh_token, db=db)
