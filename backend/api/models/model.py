"""Archivo encargado de configurar la estructura del json que se recibe"""
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


###################################

class JSONData(BaseModel):
    tex: Tex
    cls: Cls
