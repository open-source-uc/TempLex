%-------------------- COLORES --------------------
\definecolor{azulmedio}{RGB}{2,112,193}
\definecolor{grisoscuro}{RGB}{118,113,113}
\definecolor{amarillooro}{RGB}{255, 215, 0}
\definecolor{azulclaro}{RGB}{199,234,253}
\definecolor{rojoclaro}{RGB}{211, 47, 47} % some dark red
\definecolor{cian}{RGB}{0,173,239}
\definecolor{deepblue}{rgb}{0,0,0.5}
\definecolor{deepred}{rgb}{0.6,0,0}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{grey}{RGB}{128,128,128}
\definecolor{silver}{RGB}{169,169,169}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}
\definecolor{RoyalBlue}{RGB}{2,112,193}
\definecolor{azul2}{RGB}{83, 131, 155}
\definecolor{rojo2}{RGB}{243, 108, 108}
\definecolor{amarillo2}{RGB}{243, 188, 100}
\definecolor{cian2}{RGB}{93, 196, 188}
\definecolor{shadecolor}{RGB}{224,238,238}

%-------------------- ENCABEZADO --------------------
\renewcommand{\headrulewidth}{0pt} % eliminamos linea encabezado
\renewcommand{\footrulewidth}{0pt} % eliminamos linea pie pagina
\setlength\headheight{61.3pt}      % Distancia entre encabezado y contenido
\addtolength{\textheight}{-50.0pt} % Distancia entre encabezado y pie de pag

% Encabezado personalizado https://latex.org/forum/viewtopic.php?t=33369

%-------------------- OTROS --------------------
\titleformat{\section}[hang]
    {}
    {\color{RoyalBlue}\LARGE\bfseries \thesection . \ }{0pt}
    {\color{RoyalBlue}\LARGE\bfseries}
\titleformat{\subsection}[hang]
    {}
    {\color{grey}\Large\bfseries \thesubsection. \ }{0pt}
    {\color{grey}\Large\bfseries}
\titleformat{\subsubsection}[hang]
    {}
    {\color{silver}\large\bfseries \thesubsubsection. \ }{0pt}
    {\color{silver}\large\bfseries}
%\setcitestyle{square,super}


% -----------------------------------------------------
% Comandos
% -----------------------------------------------------
% Encabezado personalizado https://latex.org/forum/viewtopic.php?t=33369
\newcommand{\heading}[2]{
    \begin{tikzpicture}[remember picture, overlay]
        \node [
            fill=gray, 
            anchor=north,
            minimum width=\paperwidth, 
            minimum height=3cmheading
        ] (box) at (current page.north) [font=\Huge, text=white] {#1 #2};
        \path 
            (box.west) -- 
                node {\includegraphics[scale=.2]{example-image-a}} 
            (box.center)
        ;
    \end{tikzpicture}
    \vskip 2cm
} % \heading{Capitulo}{1:algo}


%-------------------- CONDITIONS --------------------
\newenvironment{conditions*}
  {\par\vspace{\abovedisplayskip}\noindent
   \tabularx{\columnwidth}{>{$}l<{$} @{\ : } >{\raggedright\arraybackslash}X}}
  {\endtabularx\par\vspace{\belowdisplayskip}}
% EJEMPLO: \begin{conditions*}
%           E  &  TEXTO \end{conditions*}
  
  

%-------------------- CAPTION --------------------
\captionsetup[table]{format=plain, textfont=it, font=small, justification=raggedright, labelfont=bf,labelsep=newline, skip=1pt, singlelinecheck=false}

\captionsetup[figure]{format=plain, textfont=it, font=small, justification=raggedright, labelfont=bf,labelsep=newline, skip=1pt, singlelinecheck=false}


%-------------------- EXTRA --------------------
% Desactiva errores de overfull y underfull.
\hfuzz=\maxdimen
% \tolerance=10000
\hbadness=10000


%-------------------- PANDOC --------------------
% MARKDOWN -> LaTeX: https://pandoc.org
\providecommand{\tightlist}{
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}
}

