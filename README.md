<h1 align="center">
  <br>
  <a href=# name="readme-top"><img src="./docs/img/TempLeX.svg" width="250px" alt="banner TempLeX"></a>
</h1>
<h4 align="center"> Generador de plantillas en LaTeX </h4>
<p align="center">
  <a href="#Descripción">Descripción</a> •
  <a href="#Uso">Uso</a> •
  <a href="#Contribuir">Contribuir</a> •
  <a href="#Creditos">Creditos</a> •
  <a href="#Soporte">Soporte</a> •
  <a href="#Licencía">Licencia</a>
</p>

---

## Descripción

El proyecto va a consistir en una SPA que se podría generalizar en 3 cosas principales: la interfaz web, la API y en generador de plantillas (de la mano con la api)

- Para la interfaz web no hay nada decidido de cómo se va a realizar, por lo que es algo que se puede discutir. Quizás ni siquiera sea necesario un framework, pero esta como opción usar Vite-react con tailwind css para los estilos.
De forma general, el front es un formulario que pregunta al usuario por alguna plantilla pre definida o personalizada y luego permite editar cosas como la portada, indices, columnas, letra, márgenes, si incluye tutoríal o no, etc.

- Para la API usaremos python con la librería [FastApi](https://fastapi.tiangolo.com) para manejar las solicitudes y [Gunicorn](https://gunicorn.org) como servidor. 

- Cuando se realiza una solicitud de compilación, se crea una tarea en una cola que construye una plantilla de LaTeX con ayuda de [jinja](https://jinja.palletsprojects.com/en/3.1.x) en base a un .json recibido desde el front, para luego ser comprimido en un .zip y enviado nuevamente al usuario.

> _En un futuro sería bueno ver cómo podemos pre generar algunos resultados en base a plantillas pre hechas y así quitarle algo de carga del servidor._

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## TODO

- [x] Crear la API con *Fast Api*
- [ ] Configurar API
- [ ] Mejorar el tutorial de cómo usar LaTeX que se incluye por defecto 
- [ ] Hacer un generador de .tex con *jinja*
- [ ] Convertir los [templates de OSUC](https://github.com/open-source-uc/latex-templates) en una plantilla general. 
- [ ] Estudiar como comprimir el zip y enviar los archivos al front 
- [ ] Manejó de errores y documentación de la API
- [ ] (opcional) crear la vista con Figma
- [ ] Crear la vista con algún framework de preferencia (consultarlo)
- [ ] Ver cómo optimizar la generación de archivos, buscando como pre generar algunas plantillas por defecto
- [ ] Pasar a Docker el proyecto 
- [ ] Configurar un devcontainer

## Uso


```shell
# Solo 1 vez
python3 -m venv env 
source env/bin/activate 

# Solo 1 vez (o cuando se agregan dependencias)
python -m pip install --upgrade pip
pip install -r requirements.txt
```
<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Contribuir

```shell
# Para actualizar los requirements.txt
pip freeze > requirements.txt 
```


#### Bug Reports & Feature Requests

Utilice las **issues** para informar cualquier bug o solicitud.

#### Workflow

> El workflow es PR a development -> Revisar preview y checks -> Asignar reviewers -> Aprobación -> Merge a development

La información detallada sobre cómo contribuir se puede encontrar en [contributing.md](contributing.md).


### Necesitas contactarnos
Comuníquese con nosotros a travez de [OSUC.dev](https://links.osuc.dev/)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Creditos

### Mantenedores

- [diegocostares](https://www.github.com/diegocostares)
- [](https://www.github.com/USERNAME)


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Licencía

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./license.md)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>