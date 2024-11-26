

from fastapi import FastAPI
import uvicorn
from typing import Union

# main.py
# uvicorn main:app:
app = FastAPI()
# uvicorn.run(app, host="0.0.0.0")

@app.get("/")
async def read_root():
    return {"Msg": "World"}

#ruta tipo post 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definir el modelo de datos
class Item(BaseModel):
    url: str

# Crear la ruta POST
@app.post("/items/")
async def create_item(item: Item):
    #logica del codigo
    url_imagen = item.url
    
    # LEER IMAGEN
    # MANDAR A ROBOFLOW
    # OBTENER RESPUESTA
    # RETURN DE LA RESPUESTA DE ROBOFLOW
    
#TENGO RUTA TIPO POST, HECHA EN FAST APPI
#PONER A CORRER CON UVICORN EL SERVIDOR DE FASTAPPI PARA PODER ESCUCHAR LA RUTA POST Q HICE
#CON POSTMAN PUEDO HACER UNA REQUEST AL SERVIDOR DE FASTAPI A LA RUTA TIPO POST PARA VER Q ANDE

#EN LA RUTA TIPO POST PODER RECIBIR URL LEERLA Y EVALUAR EL MODELO Y RESPONDER A LA REQUEST CON LA RTA DEL MODELO.  


    return {
        "url": url_imagen,
        "respuesta": "PARKINSON"
    }

