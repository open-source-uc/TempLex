"""
Archivo que se encarga de las funciones para generar los templates
"""
from os import path, removedirs, makedirs
import shutil
from jinja2 import Environment, FileSystemLoader
import json
import tempfile
import zipfile
import time


def generate_template(data: dict) -> None:
    """Funcion principal que se encarga de generar los templates"""
    if not data:
        raise ValueError("ERROR: No se han ingresado datos")
    files_names = ["style.cls", "main.tex",
                   "bibliografia.tex", "portada.tex", "tutorial.tex"]
    for file in files_names:
        create_latex_env(file, data)


def create_latex_env(file_name: str, data: dict) -> None:
    """Funcion encargada de configurar jinja para LaTeX"""
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
        loader=FileSystemLoader(normalize_path(file_name, False))
    )
    # Se recomienda usar archivos .tex.jinja, pero vscode no lo reconoce corectamente
    template = latex_jinja_env.get_template(file_name)  # .jinja
    # creamos el resutlado
    result = template.render(data)
    # generamos el archivo
    create_files(result, file_name)


def create_files(result: str, file_name: str) -> None:
    """La funcion renderiza el template con los datos y lo guarda en un archivo .___"""
    # guardamos
    file_path = normalize_path(file_name)
    with open(file_path, 'w+', encoding='utf-8') as f:
        f.write(result)


def normalize_path(file_name: str, result_path=True) -> str:
    """
    Funcion que normaliza el path de un archivo dependiendo del nombre
    Cuando result_path es False, se usa para las rutas de los templates que usa FileSystemLoader
    """
    if (file_name == "bibliografia.tex" or file_name == "portada.tex" or file_name == "tutorial.tex"):
        if result_path:
            file_path = path.join(path.abspath(
                '.'), "backend", "result", "content", file_name)
        else:
            file_path = path.join(path.abspath(
                '.'), "backend", "templates", "content")
    else:
        if result_path:
            file_path = path.join(path.abspath(
                '.'), "backend", "result", file_name)
        else:
            file_path = path.join(path.abspath('.'), "backend", "templates")
    return file_path


def temp_file():
    """Crea un archivo temp y retorna un .zip con los archivos en la carpeta result"""
    work_dir = path.abspath(".")
    zip_path = path.join(work_dir, "backend", "result", "template.zip")

    list_names = ["style.txt", "main.txt"]
    list_img = ["cuadradoejemplo.png", "tablaejemplo.png"]

    try:
        with tempfile.TemporaryDirectory() as zip_dir:  # Creamos una carpeta temporal
            # Creamos el archivo .zip que contendra los archivos registrados en la carpeta temporal
            with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zfd:
                print("eeeee", zip_dir)
                for file_name in list_names:
                    file_path = path.join(zip_dir, file_name)
                    # write_(file_path, file_name)
                    with open(file_path, 'w+', encoding='utf-8') as f:
                        f.write("ñe")
                    zfd.write(file_path, file_name)
                # Creamos la carpeta img dentro de zfd
                img_dir = path.join(zip_dir, "img")
                makedirs(img_dir)
                # Copiamos desde backend/templates/img/list_img[i] al zfd
                for image in list_img:
                    image_path = path.join(
                        work_dir, "backend", "templates", "img", image)
                    shutil.copy(image_path, img_dir)
                    zfd.write(path.join(img_dir, image),
                              path.join("img", image))
            return zip_path
    finally:
        print("uwu", zip_dir)
        print("FIN")


if __name__ == "__main__":
    # with open(path.join(path.abspath('.'), 'backend', 'example.json'), encoding='utf-8') as fh:
    #     data = json.load(fh)
    # print(data)
    # generate_template(data)
    temp_file()
