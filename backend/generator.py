"""
Archivo que se encarga de las funciones para generar los templates
"""
from os import path
from jinja2 import Environment, FileSystemLoader


def create_latex_env(file_name: str, data: dict) -> Environment:
    """Funcion encargada de configurar jinja para LaTeX"""
    latex_jinja_env = Environment(
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=FileSystemLoader(normalize_path(file_name, False))
    )
    # Se recomienda usar archivos .tex.jinja, pero vscode no lo reconoce corectamente
    template = latex_jinja_env.get_template(file_name)  # .jinja
    # generamos el archivo
    generate(template, data, file_name)
    return template


def generate(template: Environment, data: dict, file_name: str) -> None:
    """La funcion renderiza el template con los datos y lo guarda en un archivo .___"""
    result = template.render(data)
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


if __name__ == "__main__":
    data = {}
    files_names = ["style.cls", "main.tex",
                   "bibliografia.tex", "portada.tex", "tutorial.tex"]
    for file in files_names:
        template = create_latex_env(file, data)
