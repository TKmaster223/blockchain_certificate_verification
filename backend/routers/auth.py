from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "secret-token":  # Replace with JWT in production
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"user": "admin"}
