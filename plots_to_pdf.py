#!/usr/local/bin/python

# -*- coding: utf-8 -*-
import os, sys, subprocess, copy


class VisualPDF:
    def __init__(self):
        self.grunddokument = ""

    def get_mainfile(self, frames):
        """
        Input: frames List(String)      all plots alreadt in latex form
        Output: dokument String         hole document in latex form

        creates document, ready to be run as .tex
        """
        dokument = \
            '\documentclass[10pt]{beamer} \n \
    \hypersetup{pdfpagemode=FullScreen} \n \
    \\usepackage{tikz} \n \
    \\usetikzlibrary{shadows,patterns,shapes} \n \
    \\usetikzlibrary{shapes.arrows,chains} \n \
    % serifenfreier Font -- fuer Praesentation geeignet/er \n \
    \listfiles % damit im Log alle benutzten Pakete aufgelistet werden \n \
    \\usetheme[progressbar=frametitle]{metropolis} \n \
    \\usepackage{appendixnumberbeamer} \n \
    \\usepackage{booktabs} \n \
    \\usepackage[scale=2]{ccicons} \n \
    \\usepackage[utf8]{inputenc} \n \
    \\usepackage{pgfplots} \n \
    \\usepgfplotslibrary{dateplot} \n \
    \\usepackage[ngerman]{babel} \n \
    \\usepackage{xspace} \n \
    \\usebackgroundtemplate{\n \
    \\tikz[overlay,remember picture] \n \
    \\node[opacity=0.3, at=(current page.south east),anchor=south east,inner sep=0pt] {\n \
    \includegraphics[width=100mm]{./PDFcreater/Pictures/background.png}};\n \
    } \n \
    %\\usebackgroundtemplate{\includegraphics[,right]{./PDFcreater/Pictures/background.png}}\n \
    \\definecolor{Purple}{HTML}{6D087C}\n \
    \\definecolor{Orange}{HTML}{CF4A30}\n \
    \n \
    % Theme colors are derived from these two elements\n \
    \setbeamercolor{alerted text}{fg=Orange}\n \
    \n \
    % ... however you can of course override styles of all elements \n \
    \setbeamercolor{frametitle}{bg=Purple}\n \
    \n \
    \\title{SolidEdge Feedback der Studierenden} \n \
    \\begin{document} \n \
    \\maketitle \n'
        dokument = dokument + frames
        dokument = dokument + '\end{document}'
        return (dokument)

    def draw_frame(self):
        """
        Creates for each png file within ./PDFcreater/Plots one
        single slide within the main document
        Output: String of one plot image, on one single slide

        """
        frame = ''
        for filename in os.listdir('./PDFcreater/Plots'):
            name = filename.split('.')
            frame = frame + '\\begin{frame}[fragile]{'
            frame = frame + name[0]
            frame = frame + '} \n \
\\begin{figure}\n \
\includegraphics[width= 0.9\linewidth]{./PDFcreater/Plots/'
            frame = frame + filename
            frame = frame + '};\n \
\\end{figure}\n \
\\end{frame}\n'
        return frame

    def write_file(self, data):
        """
        Input: data String  tex-document
        writes in the .tex file and closes it
        """
        write_tex = open("Se_Feedback.tex", "w")
        write_tex.write(data)
        write_tex.close()

    def visualize(self):
        """
        executes the .tex file and saves it as NPS-Analysis-Plots.pdf
        Will be opened by default pdf viewer.
        """
        try:
            os.remove("Se_Feedback.pdf")
        except:
            pass
        print("...still running... DO NOT SHUT DOWN...")
        os.system("pdflatex Se_Feedback.tex")  # must be run twice, otherwise the backgroundimage wont be there
        os.system("pdflatex Se_Feedback.tex")
        pdf = "Se_Feedback.pdf"
        os.startfile(pdf)


