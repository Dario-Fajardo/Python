from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

@app.get("/url")
async def url():
    return { "url_youtube" : "https://www.youtube.com" }

# Documentación con Swagger: /docs
# Documentación con Redocly: /redoc