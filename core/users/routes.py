#========================= IMPORTS ==================================

from fastapi import APIRouter,Path ,Depends,HTTPException,status
from fastapi.responses import JSONResponse
from users.models import UserModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List
from datetime import datetime
from users.schemas import UserLoginSchema,UserRegisterSchema

#==================================================================



#=================== ROUTE SETUP ======================================
router = APIRouter(tags=["users"],prefix="/users")
#======================================================================



#============================= FUNCTIONS ==============================
@router.post("/login")
async def user_login(request:UserLoginSchema,db:Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == request.username).first()
    if not user:
        raise HTTPException(detail="User does not exist",status_code=status.HTTP_404_NOT_FOUND)

    if not user.verify_password(request.password):
        raise HTTPException(detail="PassWord is invalid", status_code=status.HTTP_400_BAD_REQUEST)

    return {}

@router.post("/register")
async def user_register(request:UserRegisterSchema,db:Session = Depends(get_db)):
    old_user = db.query(UserModel).filter(UserModel.username == request.username).first()
    if old_user:
        raise HTTPException(detail="This username have been taken",status_code=status.HTTP_409_CONFLICT)
    new_user = UserModel(username=request.username)
    new_user.set_password(request.password)
    db.add(new_user)
    db.commit()
    return JSONResponse(content="User Registered successfully")
