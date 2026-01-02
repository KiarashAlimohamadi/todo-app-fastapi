#========================= IMPORTS ==================================

from fastapi import APIRouter,Path ,Depends,HTTPException
from fastapi.responses import JSONResponse
from user.models import UserModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List
from datetime import datetime

#==================================================================



#=================== ROUTE SETUP ======================================
router = APIRouter(tags=["users"],prefix="/users")
#======================================================================



#============================= FUNCTIONS ==============================
@router.post("/users")
async def user_login(db:Session = Depends(get_db)):
    return {}

@router.post("/users")
async def user_register(db:Session = Depends(get_db)):
    return {}