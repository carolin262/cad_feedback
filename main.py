# -*- coding: utf-8 -*-
import matplotlib
import plots_to_pdf
import json_to_plots
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
matplotlib.style.use('ggplot')
from pylab import *

class Feedback_client:
    def __init__(self):
        json_to_plots_obj = json_to_plots.Json_parser()

        self.se_dataframe = json_to_plots_obj.se_file()
        self.se_dataframe.columns = ["id", "tutor", "fach", "text1", "text2", "gender",
                                   "semester", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9",
                                   "f10", "f11", "f12", "f13", "f14", "f15","f16"]
        #not tested yet
        self.nx_dataframe = json_to_plots_obj.nx_file()
        self.nx_dataframe.columns = ["id", "tutor", "fach", "text1", "text2", "gender",
                                     "semester", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9",
                                     "f10", "f11", "f12", "f13", "f14", "f15", "f16"]
        self.plot_all()
        """
        self.plot_barchart(self.se_dataframe,[int(i) for i in self.se_dataframe['semester'].values],
                           [int(i) for i in self.se_dataframe['semester'].values],
                           "semester","","no")
        """

    def plot_all(self):
        """
        ["id", "tutor", "fach", "text1", "text2", "gender",
            "semester", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9",
            "f10", "f11", "f12", "f13", "f14", "f15","f16"]
        """

        self.plot_gender_pie(self.se_dataframe, 'gender', 'Geschlecht_der_Studis')

        self.plot_gender_pie(self.se_dataframe, 'tutor', 'Tutor_der_Studis')

        self.plot_gender_pie(self.se_dataframe, 'fach', 'Studiengang_der_Studis')

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['semester'])[0],
                           self.sort_column(self.se_dataframe['semester'])[1],
                           "Semester_der_Studierenden", "Semester", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f2'])[0],
                           self.sort_column(self.se_dataframe['f2'])[1],
                           "Tutor_kann_den_Lehrinhalt_verstaendlich_darlegen",
                           "Verstaendnis im Tutorium", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f3'])[0],
                           self.sort_column(self.se_dataframe['f3'])[1],
                           "Tutor_ist_immer_gut_auf_das_Tutorium_vorbereitet",
                           "Vorbereitung", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f4'])[0],
                           self.sort_column(self.se_dataframe['f4'])[1],
                           "Tutor_foerdert_aktive_Teilnahme_der_Studenten",
                           "Aktive Teilnahme", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f5'])[0],
                           self.sort_column(self.se_dataframe['f5'])[1],
                           "Ich_war_immer_gut_auf_das_Tutorium_vorbereitet",
                           "Vorbereitung der Studis", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f6'])[0],
                           self.sort_column(self.se_dataframe['f6'])[1],
                           "Die_Uebungen_sind_gut_strukturiert",
                           "Struktur des Tutorium", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f7'])[0],
                           self.sort_column(self.se_dataframe['f7'])[1],
                           "Die_Uebungsbeispiele_sind_gut_gewaehlt",
                           "Beispiele sind gut", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f8'])[0],
                           self.sort_column(self.se_dataframe['f8'])[1],
                           "Der_Schwierigkeitsgrad_war_hoch",
                           "Zu schwierig", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f9'])[0],
                           self.sort_column(self.se_dataframe['f9'])[1],
                           "Ich_habe_mich_schon_fruehzeitig_mit_dem_Programm_zu_Hause_beschaeftigt",
                           "Fruehes, eigenstaendiges Arbeiten der Studis", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f10'])[0],
                           self.sort_column(self.se_dataframe['f10'])[1],
                           "Ich_habe_die_Uebungsaufgaben_alle_gemacht",
                           "Fleissige Studis", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f11'])[0],
                           self.sort_column(self.se_dataframe['f11'])[1],
                           "Ich_haette_gerne_mehr_Uebungsaufgaben_gehabt",
                           "Unterforderte Studis", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f12'])[0],
                           self.sort_column(self.se_dataframe['f12'])[1],
                           "Die Formulierungen in der Hausaufgabe waren eindeutig",
                           "Eindeutige Hausaufgaben", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f13'])[0],
                           self.sort_column(self.se_dataframe['f13'])[1],
                           "Der_Lehrinhalt_war_ausreichend_um_die_HA_zu_bearbeiten",
                           "Hausaufgaben vorbereitung war ausreichend", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f14'])[0],
                           self.sort_column(self.se_dataframe['f14'])[1],
                           "Ich_habe_viel_Zeit_zur_Bearbeitung_der_Hausaufgabe_benoetigt",
                           "langsame Studenten", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f15'])[0],
                           self.sort_column(self.se_dataframe['f15'])[1],
                           "Die_Hausaufgabe_sollte_vom_Umfang_her_reduziert_werden",
                           "Zuviele Hausaufgaben", "Anzahl an Studis")

        self.plot_barchart(self.se_dataframe, self.sort_column(self.se_dataframe['f16'])[0],
                           self.sort_column(self.se_dataframe['f16'])[1],
                           "Benoetigte_Stundenzahl_vom_gesamten_CAD_Kurs_pro_Woche",
                           "Stunden pro Woche", "Anzahl an Studis")





    def sort_column(self, column):
        #self.sort_column(self.se_dataframe['semester'])
        x = []
        y = []
        for i in column:
            if i in x:
                y[x.index(i)] += 1
            else:
                x.append(i)
                y.append(1)
        return x,y

    def plot_barchart(self,dataframe,x,y,title,xlable,ylable):
        plt.bar(x, y, color='blue')
        #plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.savefig('./PDFcreater/Plots/{}.png'.format(title))
        #loescht den Plot fuer den Naechsten Plot
        plt.clf()
        plt.cla()
        plt.close()

    def plot_scatter(self,dataframe,x,y,title,xlable,ylable):
        plt.scatter(x, y)
        #plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.savefig('./PDFcreater/Plots/{}.png'.format(title))
        plt.show()

    def plot_scatter_topic(self,se_dataframe,topic,se_title):
        gender = self.sort_column(se_dataframe[topic])
        labels = [gender[0][i] for i, elem in enumerate(gender[0])]
        fracs = [gender[1][i] for i, elem in enumerate(gender[1])]
        explode = [0.05 for i, elem in enumerate(gender[1])]
        plt.scatter([i for i, elem in enumerate(gender[1])], fracs)
        #plt.pie(fracs, explode=explode, labels=labels, autopct='%.0f%%', shadow=True)
        plt.savefig('./PDFcreater/Plots/{}.png'.format(se_title))

    def plot_gender_pie(self,se_dataframe,topic,se_title):
        gender = self.sort_column(se_dataframe[topic])
        labels = [gender[0][i] for i,elem in enumerate(gender[0])]
        fracs = [gender[1][i] for i,elem in enumerate(gender[1])]
        explode = [0.05 for i,elem in enumerate(gender[1])]
        plt.pie(fracs, explode=explode, labels=labels, autopct='%.0f%%', shadow=True)
        plt.savefig('./PDFcreater/Plots/{}.png'.format(se_title))
        plt.clf()
        plt.cla()
        plt.close()


"""
    # creates the whole document and executes it
    visual_obj=visual.VisualPDF()
    visual_obj.write_file(visual_obj.get_mainfile(visual_obj.draw_frame()))
    visual_obj.visualize()
"""

if __name__=='__main__':
    feedback_obj=Feedback_client()
    visual_obj = plots_to_pdf.VisualPDF()
    visual_obj.write_file(visual_obj.get_mainfile(visual_obj.draw_frame()))
    visual_obj.visualize()
    print("Done")

