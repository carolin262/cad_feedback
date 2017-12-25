# -*- coding: utf-8 -*-
import matplotlib
import plots_to_pdf
import json_to_plots
import matplotlib as plt
from pylab import *

class Feedback_client_Se:
    def __init__(self,kurs):
        json_to_plots_obj = json_to_plots.Json_parser()

        self.se_dataframe = json_to_plots_obj.se_file()
        self.se_dataframe.columns = ["id", "tutor", "fach", "text1", "text2", "gender",
                                   "semester", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9",
                                   "f10", "f11", "f12", "f13", "f14", "f15","f16"]
        self.plot_all_SolidEdge(kurs)

    def plot_all_SolidEdge(self, kurs):
        """
        ["id", "tutor", "fach", "text1", "text2", "gender",
            "semester", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9",
            "f10", "f11", "f12", "f13", "f14", "f15","f16"]
        """

        self.plot_pie(self.se_dataframe, 'gender', 'Geschlecht+der+Studis', kurs)

        self.plot_pie(self.se_dataframe, 'tutor', 'Tutor+der+Studis', kurs)

        self.plot_pie(self.se_dataframe, 'fach', 'Studiengang+der+Studis', kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'semester',
                           "Semester+der+Studierenden", "Semester", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f2',
                           "Tutor+kann+den+Lehrinhalt+verstaendlich+darlegen",
                           "Verstaendnis im Tutorium", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f3',
                           "Tutor+ist+immer+gut+auf+das+Tutorium+vorbereitet",
                           "Vorbereitung", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f4',
                           "Tutor+foerdert+aktive+Teilnahme+der+Studenten",
                           "Aktive Teilnahme", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f5',
                           "Ich+war+immer+gut+auf+das+Tutorium+vorbereitet",
                           "Vorbereitung der Studis", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f6',
                           "Die+Uebungen+sind+gut+strukturiert",
                           "Struktur des Tutorium", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f7',
                           "Die+Uebungsbeispiele+sind+gut+gewaehlt",
                           "Beispiele sind gut", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f8',
                           "Der+Schwierigkeitsgrad+war+hoch",
                           "Zu schwierig", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f9',
                           "Ich+habe+mich+schon+fruehzeitig+mit+dem+Programm+zu+Hause+beschaeftigt",
                           "Fruehes, eigenstaendiges Arbeiten der Studis", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f10',
                           "Ich+habe+die+Uebungsaufgaben+alle+gemacht",
                           "Fleissige Studis", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f11',
                           "Ich+haette+gerne+mehr+Uebungsaufgaben+gehabt",
                           "Unterforderte Studis", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f12',
                           "Die+Formulierungen+in+der+Hausaufgabe+waren+eindeutig",
                           "Eindeutige Hausaufgaben", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f13',
                           "Der+Lehrinhalt+war+ausreichend+um+die+HA+zu+bearbeiten",
                           "Hausaufgaben vorbereitung war ausreichend", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f14',
                           "Ich+habe+viel+Zeit+zur+Bearbeitung+der+Hausaufgabe+benoetigt",
                           "langsame Studenten", "Anzahl an Studis", kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f15',
                           "Die+Hausaufgabe+sollte+vom+Umfang+her+reduziert+werden",
                           "Zuviele Hausaufgaben", "Anzahl an Studis",kurs)

        self.plot_stacked_barchart(self.se_dataframe, 'f16',
                           "Benoetigte+Stundenzahl+vom+gesamten+CAD+Kurs+pro+Woche",
                           "Stunden pro Woche", "Anzahl an Studis", kurs)





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

    def plot_boring_barchart(self,dataframe,x,y,title,xlable,ylable, kurs):
        plt.bar(x, y, color='blue')
        #plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.savefig('./PDFcreater/Plots/{}/{}.png'.format(kurs,title))
        #loescht den Plot fuer den Naechsten Plot
        plt.clf()
        plt.cla()
        plt.close()

    def plot_scatter(self,dataframe,x,y,title,xlable,ylable,kurs):
        plt.scatter(x, y)
        #plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.savefig('./PDFcreater/Plots/{}/{}.png'.format(kurs,title))
        plt.show()

    def plot_stacked_barchart(self, dataframe, sort, title, xlable, ylable, kurs):
        x = []
        tutor=[]
        y = []
        for i in dataframe['tutor']:
            if i not in tutor:
                tutor.append(i)
                y.append([])

        for i,elem in enumerate(dataframe[sort]):
            print(y, elem)
            if elem in x:
                y[tutor.index(dataframe['tutor'][i])][x.index(elem)] += 1
            else:
                x.append(elem)
                for j,elem2 in enumerate(tutor):
                    y[j].append(0)
                y[tutor.index(dataframe['tutor'][i])][x.index(elem)] += 1

        for i,elem in enumerate(y):
            plt.bar(range(len(elem)), elem, label=tutor[i])
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.legend(loc="best")
        plt.savefig('./PDFcreater/Plots/{}/{}.png'.format(kurs,title))
        #plt.show()
        # loescht den Plot fuer den Naechsten Plot
        plt.clf()
        plt.cla()
        plt.close()

    def plot_pie(self, se_dataframe, topic, se_title, kurs):
        gender = self.sort_column(se_dataframe[topic])
        labels = [gender[0][i] for i,elem in enumerate(gender[0])]
        fracs = [gender[1][i] for i,elem in enumerate(gender[1])]
        explode = [0.05 for i,elem in enumerate(gender[1])]
        plt.pie(fracs, explode=explode, labels=labels, autopct='%.0f%%', shadow=True)
        plt.savefig('./PDFcreater/Plots/{}/1{}.png'.format(kurs,se_title))
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
    feedback_obj=Feedback_client_Se('SolidEdge')
    visual_obj = plots_to_pdf.VisualPDF(feedback_obj.se_dataframe, 'SolidEdge')
    visual_obj.write_file(
        visual_obj.get_mainfile(
            visual_obj.draw_frame('SolidEdge'),
            visual_obj.draw_comments(feedback_obj.se_dataframe, 'SolidEdge'),
            feedback_obj.se_dataframe,
            'SolidEdge'),
        'SolidEdge')
    visual_obj.visualize('SolidEdge')
    print("Done")

