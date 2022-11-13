%-------------------- MATEMATICAS --------------------
\newcommand{\R}{\mathbb{R}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\newcommand{\ele}{\mathcal{L}}
\newcommand{\F}{\mathcal{F}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}
\newcommand{\D}{\mathcal{D}}
\newcommand{\doubleoverline}[1]{\overline{\overline{#1}}}
\renewcommand{\(}{\left(}
\renewcommand{\)}{\right)}
\renewcommand{\[}{\left[}
\renewcommand{\]}{\right]}
\newcommand{\foral}{\;\forall\;}
\newcommand{\exist}{\;\exists\;}
\renewcommand{\exists}{\;\exists\; }
\newcommand{\contr}{\rightarrow\leftarrow}
\renewcommand{\phi}{\varphi}
%\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}

%-------------------- COMANDOS IMAGENES Y TABLAS --------------------
% Configuracion imagenes
\newcommand{\fig}[4][\relax]{
  \begin{figure}[H]
    \centering
    \begin{measuredfigure}
        \ifx\relax#1\else\label{img:#1}\fi
        \ifx\relax#2\else\caption{#2}\fi
        \includegraphics[#3]{#4}%
    \end{measuredfigure}
  \end{figure}%
}
% Configuracion imagenes a la izquierda o derecha
\newcommand{\figposition}[5][\relax]{
    \begin{wrapfigure}{#5}{0.25\textwidth} % Margen texto 0.25
        \centering
        \begin{measuredfigure}
            \ifx\relax#1\else\label{img:#1}\fi
            \ifx\relax#2\else\caption{#2}\fi
            \includegraphics[#3]{#4} %[scale=0.1]
        \end{measuredfigure}
    \end{wrapfigure}
}
% Configuracion de tablas con imagenes:
\newcommand{\tableimage}[5][\relax]{
    \begin{table}[H]
        \centering
        \begin{measuredfigure}
            \label{Tab:#1}
            \caption{#2}
            \includegraphics[#3]{#4} 
        \end{measuredfigure}
        \\ \textit{\scriptsize{#5}}
    \end{table}
}

