%-------------------- PYTHON STYLE --------------------
% Python style for highlighting
\newcommand\pythonstyle{\lstset{
language=Python,
basicstyle=\ttb,
otherkeywords={self},  % Add keywords here
keywordstyle=\ttb\color{deepblue},
emph={MyClass,__init__},          % Custom highlighting
emphstyle=\ttb\color{deepred},    % Custom highlighting style
stringstyle=\color{deepgreen},
frame=tb,                         % Any extra options here
showstringspaces=false,
 % 
}}
% Python environment
\lstnewenvironment{python}[1][]{
\pythonstyle
\lstset{#1}
}{}
% Python for external files
\newcommand\pythonexternal[2][]{{
\pythonstyle
\lstinputlisting[#1]{#2}}}

% Python for inline
\newcommand\pythoninline[1]{{\pythonstyle\lstinline!#1!}}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{grey},
    rulecolor =\color{black},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    frame = single, %L
    %keeppaces = true,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
}
\lstdefinestyle{stylepython}{
  belowcaptionskip=1\baselineskip,
  breaklines=true,
  %frame=L,
  xleftmargin=\parindent,
  showstringspaces=false,
  basicstyle=\ttfamily\footnotesize,
  keywordstyle=\bfseries\color{green!40!black},
  commentstyle=\itshape\color{grey},,
  identifierstyle=\color{blue},
  stringstyle=\color{orange},
  captionpos=b,
  numbers=left,   
  numberstyle=\color{grey},
  numbersep=-5pt,
  tabsize=2, 
}
\lstdefinestyle{blancoynegro}{% REQUIERE POENR UN TAB
  belowcaptionskip=1\baselineskip,
  xleftmargin=\parindent,
  showstringspaces=false,
  basicstyle=\ttfamily\footnotesize,
  %captionpos=b,
  numbers=left,   
  identifierstyle=\color{black},
  numberstyle=\color{grey},
  numbersep=-5pt,
  tabsize=2, 
}

\lstdefinestyle{customasm}{
  belowcaptionskip=1\baselineskip,
  frame=L,
  xleftmargin=\parindent,
  language=[x86masm]Assembler,
  basicstyle=\footnotesize\ttfamily,
  commentstyle=\itshape\color{purple!40!black},
}

%\lstset{escapechar=@,style=customc}

%EJEMPLO: \lstinputlisting[language=Python, style=mystyle, caption=\textit{Modelo hecho con gurobi en python}, label=modelogurobi]{programa.py}

