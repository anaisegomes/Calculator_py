from tkinter import *
from tkinter import ttk


#color

cor1= "#0a0a0a" # black
cor2 = "#f7f7f7" #White
cor3 = "#87a8de"  #blue
cor4 = "#2d2d2e" #cinza
cor5 = "#a36936"  #orange


janela = Tk()
janela.title("Calculator")
janela.geometry("235x318")
janela.config(background=cor1)

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

janela.mainloop()


