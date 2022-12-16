"""Archivo encargado de configurar las rutas de la API"""
from fastapi import APIRouter
from pydantic import BaseModel


class Encabezado(BaseModel):
	visible: bool
	escuela: str
	departamento: str
	derecha: bool
	imagenderecha: str


class Portada1(BaseModel):
	escuela: str
	departamento: str
	titulo: str
	numero: str
	grupo: str
	integrantes: str
	fecha: str


class Portada(BaseModel):
	visible: bool
	portada1: Portada1
	includepdf: bool
	pdfname: str


class Indices(BaseModel):
	visible: bool
	tablas: bool
	figuras: bool
	codigo: bool


class Bibliografia(BaseModel):
	visible: bool
	estilo: str


class Tex(BaseModel):
	encabezado: Encabezado
	portada: Portada
	indices: Indices
	espaciado: float
	tutorial: bool
	bibliografia: Bibliografia

class Cls(BaseModel):
	tipography: str


template = APIRouter()

@template.get("/")
def helloworld():
	return {"message": "Hello World"}


@template.get("/template/")
async def get_template(tex: Tex, cls: Cls):
	template = {
		"tex": tex,
		"cls": cls
	}
	return template
