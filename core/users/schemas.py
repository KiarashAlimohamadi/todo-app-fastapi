from pydantic import BaseModel,Field,field_validator
from typing import Optional
from datetime import datetime


class UserLoginSchema(BaseModel):
    username : str = Field(...,max_length=250,min_length=3,description="username for login")
    password : str = Field(...,description="password for login")

class UserRegisterSchema(BaseModel):
    username : str = Field(...,max_length=250,min_length=3,description="username for register")
    password : str = Field(...,description="password for register")
    password_confirm : str = Field(...,description="password confirm for register")

    @field_validator("password_confirm")
    def passwords_checker(cls,password_confirm,validation):
        if not (password_confirm == validation.data.get("password")):
            raise ValueError("passwords are not same")
        return password_confirm
