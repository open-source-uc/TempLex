"""Archivo encargado de configurar las rutas de la API"""
from fastapi import APIRouter

template = APIRouter()

@template.get("/")
def helloworld():
	return {"message": "Hello World"}
