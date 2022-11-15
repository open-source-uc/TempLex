# DOCUMENTACION BACKEND

## Valores del json
Aca se explicaran los valores que resive el generador.

```json
{
	"tex": { // Para hacer referencia a los archivos que terminan en .tex
		"encabezado": {
			"visible": true, // Si incluye o no el encabezado
			"escuela": "ESCUELA DE INGENIERÍA",
			"departamento": "DEPARTAMENTO DE CIENCIA DE LA COMPUTACIÓN", // Puede no incluirse
			"derecha": true, // Si incluye un encabezado a la derecha
			"imagenderecha": "IMAGEN.png" // Nombre del archivo a incluir a la derecha TODO: Añadir soporte para inclir imagen en la carpetas de la plantilla
		},
		"portada": {
			"visible": true,
			"portada1": { // Opcion 1: crea una portada generica y personalizada
                "escuela": "ESCUELA DE INGENIERÍA",
                "departamento": "DEPARTAMENTO DE CIENCIA DE LA COMPUTACIÓN",
                "titulo": "Nombre del proceso",
                "numero": "Informe 1",
                "grupo": "Grupo XX",
                "integrantes": "Nombre1, Nombre2, Nombre3",
                "fecha": "<día> de <mes> de <año>"
            },
			"includepdf": true,  // Opcion 2: subir un pdf como portada tamaño carta de EEUU
			"pdfname": "Portada.pdf" // nombre del archivo subido TODO: añadir soporte a incluir en el .zip
		},
		"indices": {
            "visible": true, // Es visible el indice de contenido?
            "tablas": true, // Incluye indice de tablas?
            "figuras": true, // Incluye indice de figuras?
            "codigo": false // Incluye indice de codigo?
        },
        "espaciado": 1.15, // Espaciado del texto
        "tutorial": true, // Incluye un tutorial?
        "bibliografia": {
            "visible": true, // Incluye apartado para bibliografia?
            "estilo": "manual" // Estilos: manual (se escribe como siempre), bibtex (bibliografia automatica de LaTeX)
		},
	},
	"cls": { // Para hacer referencia a los que terminan en .cls
		"tipography": "lmodern" // Opciones: "times"(times new roman), "latin"(latin modern), "montserrat", none(default)
	} 
}
```

## Funciones de `generator.py`

Lo mas importante a mencionar es que la funcion `generate_template(data)` recibe un json y se encarga de crear un .zip que es retornado dentro de la clase `tempfile._TemporaryFileWrapper`. Para acceder al valor y trabajar con la API va a ser necesario usar el valor_retornado.name para modificarlo.