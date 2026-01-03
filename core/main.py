#========================== IMPORTS ========================

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.params import Depends
from sqlalchemy.sql.annotation import Annotated
from auth.basic_auth import get_authenticated_user
from tasks.routes import router as tasks_routes
from users.routes import router as users_route
from users.models import UserModel
from auth.token_auth import get_authenticated_user_by_token

#=============================================================



#===================== LIFE SPAN =============================
@asynccontextmanager
async def lifespan(app:FastAPI):
    print("started")
    yield
    print("shut down")
#==============================================================



#=============== SETUP =========================================
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_routes)
app.include_router(users_route)
#==============================================================



#================= FUNCTIONS ==================================
@app.get("/public")
def public_route():
    return {"message":"public message"}

@app.get("/private")
def private_route(user:UserModel = Depends(get_authenticated_user_by_token)):
    print(user)
    return {"message":"private message"}
#==============================================================
