from typing import List
from fastapi import Depends, HTTPException, APIRouter
from ..controllers.auth import create_jwt_token, check_jwt_token
from ..models.pydantic_schemas import User, UserCreate, UserLogin, UserLogged, Token


auth_route = APIRouter(prefix="/auth")
secret_key = "secret"
expires_delta = timedelta(days=15)


@auth.route.post("/get_token", response_model=Token)
def post_generate_token(user: User):
    """Generate a token for a user"""
    return create_jwt_token(user, secret_key, expires_delta)

@auth_route.post("/check_token")
def post_check_token(token: str = Depends(check_jwt_token)):
    """Check if a token is valid"""
    return check_jwt_token(token, secret_key)


