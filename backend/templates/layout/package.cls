%----------------------------- TEXTO ---------------------------
%\usepackage{mathptmx}                        % Tipografia Times New Roman
\usepackage{lmodern}                        % Tipografia Latin modern
%\usepackage[defaultfam,tabular,lining]{montserrat} % Alternativa a avenir

\usepackage[LY1]{fontenc}                   % Fuentes (Alternativa [T1])

\RequirePackage{parskip}                    % Permite separar los párrafos y configura la sangria
%\setlength{\parindent}{4em}     % sangria especifica
%\setlength{\parskip}{1em}      % Distancia parrados
\RequirePackage{setspace}                   % interlineado
\setstretch{1.15}                           % Config de interlineado
\RequirePackage{xspace}                     % Agregar espacios automáticamente después de las palabras comandos
\RequirePackage{lscape}
\RequirePackage{dirtytalk}                  % Poner cosas entre comillas fácilmente: \say{algo que va entre comillas}
\RequirePackage{ulem}                       % Tachar texto
\RequirePackage{bold-extra}                 % Monoespaciado con negrilla
\RequirePackage{textcomp}                   % Símbolos: $, copyright, ...
\RequirePackage{inputenc}                   % carácteres acentuados.
\RequirePackage{mfirstuc}                   % Agrega comandos para mayúsculas
\RequirePackage{microtype}                  % Permite un estilo mas agradable
\RequirePackage{fancyhdr}                   % Para configurar encabezado
\pagestyle{fancy}
\RequirePackage[absolute,overlay]{textpos}
\RequirePackage{soul}                       % Resaltar texto y otras cosas
%-------------------------- ECUACIONES --------------------------
\RequirePackage{amsmath,amsthm,mathtools, amssymb,amsfonts,mathrsfs,latexsym,stmaryrd}
%--------------------------- IMÁGENES ---------------------------
\RequirePackage{threeparttable}             % Permite alinear imagenes con el caption
\RequirePackage{float}                      % Posicionar figuras: H, h!, b...
\RequirePackage{graphicx}                   % Agregar características a las imágenes 
\RequirePackage{epsfig}                     % Paquete relacionado con graphicx (es una especie de envoltorio)
\RequirePackage{caption}                    % Agregar caption a las figuras
\RequirePackage{subcaption}                 % Agregar caption a las subfiguras
%\RequirePackage{epstopdf}                   % Permite agregar .eps al enunciado - WARNING->LuaLaTeX
\RequirePackage{tikz}                       % tikzpicture para imagen fondo
\RequirePackage{wrapfig}                    % Imagenes con texto al rededor
%---------------------------- TABLAS ----------------------------
\RequirePackage{tabularx}                   % Permite juntar celdas en las tablas
\RequirePackage{booktabs}                   % Tablas bonitas: toprule, midrule, bottomrule
%---------------------------- CÓDIGO ----------------------------
\RequirePackage{minted}                     % Código monoespaciado de color
\RequirePackage{listings}                   % ingresar codigos e.g. MATLAB, Python
%----------------------------- COLOR ----------------------------
\RequirePackage{color}                      % Crear y agregar colores
\RequirePackage{xcolor}                     % Colores avanzados
%----------------------------- OTROS ----------------------------
\RequirePackage[most]{tcolorbox}            % Genera cajas de colores
\RequirePackage{ifthen}                     % Hacer if dentro de latex
\RequirePackage[shortlabels]{enumitem}      % Permite personalizar enumerate, itemize y description
\RequirePackage{dirtree}                    % Generar el árbol de directorios
\RequirePackage[colorlinks=true, linkcolor=black, urlcolor=blue]{hyperref}        % Permite remover el color y borde de los links
% \RequirePackage[colorlinks = true,allcolors = black,urlcolor=blue]{hyperref}  % Vínculos 
%https://tex.stackexchange.com/questions/26071/how-can-i-have-colored-and-underlined-links-with-hyperref
\RequirePackage{multicol}                   % Permite utilizar multi-columnas
% \RequirePackage{scrextend}                % Para hacer hacer referencia a un footnote en varias partes del texto. 
                                            % IMPORTAR SOLO SI ES NECESARIO
\RequirePackage[per-mode = symbol]{siunitx}	% Unidades del S.I.U
\RequirePackage{commath}                    % Configura el espacio tipográfico por estética
\urlstyle{same} % rm sf o tt
%\RequirePackage{subfigure}                 % Entorno de multiples figuras
\RequirePackage{bm}                         % Mejora espaciado y acentuacion mate

\RequirePackage{pdfpages}                   % insertar pdfs ya creados
\RequirePackage{titlesec}                   % Define formatos para \section y +
%\RequirePackage[backend=biber,style=apa]{biblatex}
\RequirePackage{natbib}                     % Referencias bibliograficas mas comodas

% \RequirePackage[none]{hyphenat}           %  Evita que las palabras se corten(Puede verse mal)
\usetikzlibrary{mindmap}                    %,trees,intersections,arrows,automata
\RequirePackage{longtable}
\RequirePackage{nccmath}
\RequirePackage{lipsum}                     % Lorem (texto random)
\RequirePackage{array}                      % organizar por filas y columnas
%\RequirePackage{pgfplots} warning
\RequirePackage{tikz-cd}
\RequirePackage{etoolbox}
\RequirePackage{framed}
\RequirePackage{placeins}

%--- tikz library
\usetikzlibrary{automata}
\usetikzlibrary{positioning}
\usetikzlibrary{arrows} 
\usetikzlibrary{calc}

