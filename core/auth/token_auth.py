from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from users.models import UserModel,TokenModel
from core.database import get_db
from sqlalchemy.orm import Session


security = HTTPBearer(scheme_name="Token")


def get_authenticated_user_by_token(credentials: HTTPAuthorizationCredentials= Depends(security), db:Session = Depends(get_db)):
    token_obj = db.query(TokenModel).filter(TokenModel.token==credentials.credentials).one_or_none()
    if not token_obj :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credentials are not provided",
        )

    return token_obj.user