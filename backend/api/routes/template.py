"""Archivo encargado de configurar las rutas de la API"""
from os import makedirs, path, system, unlink

from api.models.model import JSONData
from fastapi import (APIRouter, FastAPI, File, HTTPException, Response,
                     UploadFile)
from generator import generate_template

template = APIRouter()


@template.get("/")
def helloworld():
    return {"message": "Hello World"}


# Funcion que se encarga de recibir un json desde el cliente y devolver un archivo .zip
@template.post("/template/")
async def process_json(json_data: JSONData):
    # TODO: validar los datos del JSON HTTPException o con el archivo exceptions.py

    try:
        # crea el archivo .zip con los datos del JSON
        zip_temp_file = generate_template(json_data)
        # envía el archivo .zip de vuelta al cliente
        return Response(content=zip_temp_file.read(), media_type="application/zip")
    finally:
        # elimina el archivo temporal
        zip_temp_file.file.close()
        unlink(zip_temp_file.name)
