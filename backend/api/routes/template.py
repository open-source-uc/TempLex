"""Archivo encargado de configurar las rutas de la API"""
from fastapi import APIRouter, FastAPI, File, UploadFile, HTTPException
from backend.api.models.model import JSONData
from backend.generator import generate_template


template = APIRouter()


@template.get("/")
def helloworld():
    return {"message": "Hello World"}


# Funcion que se encarga de recibir un json desde el cliente y devolver un archivo .zip
@template.post("/template/")
async def process_json(json_data: JSONData):
    # TODO: validar los datos del JSON HTTPException o con el archivo exceptions.py

    # crea el archivo .zip con los datos del JSON
    zip_bytes = generate_template(json_data)
    zip_file = UploadFile(filename="mi_archivo.zip",
                          content_type="application/zip")
    zip_file.file = zip_bytes

    # envía el archivo .zip de vuelta al cliente
    return {"zip_file": zip_file}
