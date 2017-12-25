#!/usr/local/bin/python

# -*- coding: utf-8 -*-
import os, sys, subprocess, copy
import numpy


class VisualPDF:
    def __init__(self, dataframe, kurs):
        self.grunddokument = ""
        self.dataframe = dataframe
        self.kurs =kurs

    def get_mainfile(self, frames, comments, dataframe, kurs):
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
    \includegraphics[width=1.53\\textwidth]{./PDFcreater/Pictures/background.png}};\n \
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
    \\title{'
        dokument = dokument + 'Feedback der Studierenden im Kurs: ' + kurs
        dokument = dokument + ' } \n \
    \\begin{document} \n \
    \\maketitle \n'
        dokument = dokument + frames
        dokument = dokument + comments
        dokument = dokument + '\end{document}'
        return (dokument)

    def draw_frame(self, kurs):
        """
        Creates for each png file within ./PDFcreater/Plots one
        single slide within the main document
        Output: String of one plot image, on one single slide

        """
        frame = ''
        for filename in os.listdir('./PDFcreater/Plots/{}/'.format(kurs)):
            name = filename.split('.')
            frame = frame + '\\begin{frame}[fragile]{'
            frame = frame + name[0].replace('+',' ')
            frame = frame + '} \n \
\\begin{figure}\n \
\includegraphics[width= 0.9\linewidth]{./PDFcreater/Plots/'
            frame = frame +'{}/'.format(kurs)
            frame = frame + filename
            frame = frame + '};\n \
\\end{figure}\n \
\\end{frame}\n'
        return frame

    def draw_comments(self, dataframe, kurs):
        """
        Creates for each png file within ./PDFcreater/Plots one
        single slide within the main document
        Output: String of one plot image, on one single slide

        """
        frame = ''
        for i, comment in enumerate(dataframe['text1']):
            if str(comment) != 'nan':
                frame = frame + '\\begin{frame}[fragile]{Kommmentare der Studenten, Tutor: '
                frame = frame + dataframe['tutor'][i] + '}'
                frame = frame + comment.replace('#', ' ').replace('&', ' ').replace('\n',' ').replace('+', ' ').replace('-',' ')
                frame = frame + ';\n \
\\end{frame}\n'
        for i,comment in enumerate(dataframe['text2']):
            if str(comment) != 'nan':
                frame = frame + '\\begin{frame}[fragile]{Kommmentare der Studenten, Tutor:'
                frame = frame + dataframe['tutor'][i] + '}'
                frame = frame + comment.replace('#', ' ').replace('&', ' ').replace('\n', ' ').replace('+',' ').replace('-', ' ')
                frame = frame + ';\n \
\\end{frame}\n'
        return frame

    def write_file(self, data, kurs):
        """
        Input: data String  tex-document
        writes in the .tex file and closes it
        """
        write_tex = open("{}_Feedback.tex".format(kurs), "w")
        write_tex.write(data)
        write_tex.close()

    def visualize(self, kurs):
        """
        executes the .tex file and saves it as NPS-Analysis-Plots.pdf
        Will be opened by default pdf viewer.
        """
        try:
            os.remove("{}_Feedback.pdf".format(kurs))
        except:
            pass
        print("...still running... DO NOT SHUT DOWN...")
        os.system("pdflatex {}_Feedback.tex".format(kurs))  # must be run twice, otherwise the backgroundimage wont be there
        os.system("pdflatex {}_Feedback.tex".format(kurs))
        pdf = "{}_Feedback.pdf".format(kurs)
        os.startfile(pdf)


