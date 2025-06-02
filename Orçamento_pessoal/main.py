from tkinter import *
from tkinter import Tk, ttk

# ----------------------------------- Cores -----------------------------------------------

co0 = "#000000"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#42535e"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

#----------------------------------- Criando janela ---------------------------------------
janele = Tk()
janele.title()
janele.geometry('900x650')
janele.config(background=co0)
janele.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janele)
style.theme_use("clam")

# criando Frame para diviaso da tela
frameCima = Frame(janele,width=1043, height=50, bg=co3, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janele,width=1043, height=361, bg=co3, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janele,width=1043, height=300, bg=co3, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

janele.mainloop()