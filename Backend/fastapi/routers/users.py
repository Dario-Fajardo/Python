from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2, OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "272a0d1f75c3f86cd382df2e8688109b826adee857b60570b2ba548634885043"

router = APIRouter(responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl = "login")

crypt = CryptContext(schemes = ["bcrypt"])

# Entidad usuario
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool


class UserDB(User):
    password: str

# Emulamos una base de datos falsa para obtener los usuarios
users_db = {
    "patatamacarron": {
        "username" : "patatamacarron",
        "fullname": "Darío Fajardo",
        "email": "ladamada18@gmail.com",
        "disabled": False,
        "password": "$2a$12$zoGGDeca/ZNtgIMIZle.huQhSbg00j6RBH7Y49ptXLI9B67Wt65na"
    },
    "josemanuel69": {
        "username": "josemanuel69",
        "fullname": "Jose Manuel Fernández",
        "email": "josemanuel69@gmail.com",
        "disabled": True,
        "password": "$2a$12$9px6c56opqdy1D5kKYBOR.TgnJOg2KzPWtMKGLHjHn9y7x801FRma"
    }           
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                              detail = "Credenciales de autenticación inválidas",
                              headers = {"WWW-Authenticate": "bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms = ALGORITHM).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "Usuario inactivo")
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "El usuario no existe")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "La contraseña no es correcta")
    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    
    return{"access_token": jwt.encode(access_token, SECRET, algorithm = ALGORITHM), "token_type": "bearer"}

@router.get("/profile")
async def me(user: User = Depends(current_user)):
    return user