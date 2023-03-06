from fastapi import APIRouter
from controllers.users import get_all_users

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the Users API"}

@router.get("/findAll")
async def find_all():
    return await get_all_users()

