from fastapi import FastAPI
from typing import Union
from routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

@app.get("/url")
async def url():
    return { "url_youtube" : "https://www.youtube.com" }

# Documentación con Redocly: /redoc
# Documentación con Swagger: /docs