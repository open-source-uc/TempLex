"""
Archivo que se encarga de las funciones para generar los templates
"""
from os import path, chdir
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
        loader=FileSystemLoader(
            path.join(path.abspath('.'), 'backend', 'templates'))
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
    with open(path.join(path.abspath('.'), "backend", "result", file_name), 'w+', encoding='utf-8') as f:
        f.write(result)


if __name__ == "__main__":
    data = {}
    file_name = "style.cls"  # "main.tex"
    template = create_latex_env(file_name, data)
