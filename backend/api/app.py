"""
Archivo principal de la API
DOCUMENTACIÓN: http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI
from api.routes.template import template

app = FastAPI(
	title="API TempLex",
	description="API encargada de generar plantillas de LaTeX a partir de un JSON",
	version="0.1.0",
	# openapi_tags=[{
	# 	"name": "Template",
	# 	"description": "Template operations"
	# }]
)

app.include_router(template)

