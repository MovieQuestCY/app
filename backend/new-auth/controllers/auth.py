from ..models import pydantic_schemas
from sqlalchemy.orm import Session
import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status

secret_key = "secret"
expires_delta = timedelta(days=15)

def check_jwt_token(token, secret_key):
    """Check if a JWT token is valid"""
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Signature has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
                            

def create_jwt_token(user: pydantic_schemas.User, secret_key: str, expires_delta: timedelta):
    """Create a JWT token for a user"""
    to_encode = {"sub": user.email, "exp": datetime.utcnow() + expires_delta}
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")
    return encoded_jwt