"""
Archivo que se encarga de las funciones para generar los templates
"""
from os import path
from jinja2 import Environment, FileSystemLoader


def create_latex_env() -> Environment:
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
    template = latex_jinja_env.get_template('main.tex')  # .jinja
    return template


def generate(data: dict):
    """Funcion encargada de generar el template"""
    print(template.render(data))


if __name__ == "__main__":
    data = {"section1": "Hola", "section2": "Mundo"}
    template = create_latex_env()
    generate(data)
