"""
Archivo que se encarga de las funciones para generar los templates
"""
from os import path, makedirs, unlink, system
import shutil
from jinja2 import Environment, FileSystemLoader
import json
import traceback
import tempfile
import zipfile
import time


def generate_template(data: dict, url=None) -> tempfile._TemporaryFileWrapper:
    """Funcion principal que se encarga de generar los templates"""
    if not data:
        raise ValueError("ERROR: No se han ingresado datos")
    list_templates = ["style.cls", "main.tex",
                      "bibliografia.tex", "portada.tex", "tutorial.tex"]
    list_images = ["cuadradoejemplo.png",
                   "tablaejemplo.png", "logo-uc-3.pdf", "logo-uc-4.pdf"]
    # TODO: Filtrar listas segun la data... ejemplo: print(data["tex"]["portada"]["visible"])
    # recibe el path donde estara el .zip
    try:
        zip_file = temp_file(data, list_templates, list_images)

        ###########################################
        # OPCIONAL: Guardamos el archivo en la carpeta result para testear
        zip_path_finally = path.join(
            path.abspath("."), "backend", "result", "template.zip")
        shutil.copy(zip_file.name, zip_path_finally)
        ###########################################

        return zip_file
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return None
    # finally:
       # unlink(zip_file.name)  # Pasar a la funcion final de donde se use


def temp_file(data: dict, list_templates: list, list_images: list) -> tempfile._TemporaryFileWrapper:
    """
    Crea un archivo(.zip) y una carpeta temporal. Procesa los archivos con con create_latex_env en la
    carpeta temporal, los escribe en el .zip y retorna el archivo temporal.
    """
    work_dir = path.abspath(".")
    # Creamos un .zip temporal con la opcion delete=False para que no se borre al cerrar
    zip_temp = tempfile.NamedTemporaryFile(
        suffix=".zip", prefix="template", delete=False, dir='/tmp')
    with tempfile.TemporaryDirectory() as zip_dir:  # Creamos una carpeta temporal
        # Creamos el archivo .zip que contendra los archivos registrados en la carpeta temporal
        with zipfile.ZipFile(zip_temp.name, "w", compression=zipfile.ZIP_DEFLATED) as zfd:
            # Creamos la carpeta img y content dentro de zfd
            img_dir = create_directory("img", zip_dir)
            create_directory("content", zip_dir)
            # Creamos y guardamos los archivos .tex y .cls
            for file_name in list_templates:
                path_file = create_latex_env(file_name, data, zip_dir)
                zfd.write(path_file, file_name)

            # Copiamos las imagenes al zfd
            for image in list_images:
                image_path = path.join(
                    work_dir, "backend", "templates", "img", image)
                shutil.copy(image_path, img_dir)
                zfd.write(path.join(img_dir, image),
                          path.join("img", image))
    return zip_temp


def create_latex_env(file_name: str, data: dict, file_path: str) -> str:
    """Funcion encargada de configurar jinja para LaTeX, obtener el contenido y guardar el archivo"""
    latex_jinja_env = Environment(
        block_start_string='((*',    # '\BLOCK{',
        block_end_string='*))',      # '}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='((#',  # '\#{',
        comment_end_string='=))',    # '}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=FileSystemLoader(
            normalize_path(file_name, path.abspath("."), False)
        )
    )
    # Se recomienda usar archivos .tex.jinja, pero vscode no lo reconoce corectamente
    template = latex_jinja_env.get_template(file_name)  # .jinja
    # creamos el resutlado
    result = template.render(data)
    # generamos el archivo
    return create_files(result, file_name, file_path)


def create_files(result: str, file_name: str, file_path) -> str:
    """Recibe los datos y lo guarda en un archivo file_name en la ruta file_path. 
    Retorna la ruta del archivo"""
    # guardamos
    file_path = normalize_path(file_name, file_path)
    with open(file_path, 'w+', encoding='utf-8') as f:
        f.write(result)
    return file_path


def normalize_path(file_name: str, start_path: str, result_path=True) -> str:
    """
    Funcion que normaliza el path de un archivo dependiendo del nombre.
    Cuando result_path es False, se usa para las rutas de los templates que usa FileSystemLoader
    """
    if (file_name == "bibliografia.tex" or file_name == "portada.tex" or file_name == "tutorial.tex"):
        if result_path:
            file_path = path.join(start_path, "content", file_name)
        else:
            file_path = path.join(start_path, "backend",
                                  "templates", "content")
    else:
        if result_path:
            file_path = path.join(start_path, file_name)
        else:
            file_path = path.join(start_path, "backend", "templates")
    return file_path


def create_directory(name, path_file) -> str:
    """Crea un directorio en la ruta especificada"""
    if path_file:
        directory = path.join(path_file, name)
    else:
        directory = name
    makedirs(directory)
    return directory


def pandoc_convert(path_file: str, name_input: str) -> str:
    """Convierte un archivo .md o .docx a .tex usando pandoc y retorna el path del archivo."""
    suffix = name_input.split(".")[1]
    if suffix != "md" or suffix != "docx":
        raise ValueError("El archivo no es .md o .docx")
    if suffix == "md":
        value = "markdown"
    else:
        value = "docx"
    path_result = path.join(path_file,  "pandoc.tex")
    system(
        f'cd {path_file} && pandoc -f {value} -t latex "{name_input}" -o "{path_result}"')
    return path_result


if __name__ == "__main__":
    with open(path.join(path.abspath('.'), 'backend', 'example.json'), encoding='utf-8') as fh:
        data = json.load(fh)
    generate_template(data)
