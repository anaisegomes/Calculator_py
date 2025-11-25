from tkinter import *
from tkinter import ttk


#color

cor1= "#0a0a0a" # black
cor2 = "#f7f7f7" #White
cor3 = "#87a8de"  #blue
cor4 = "#A8A8AC" #cinza
cor5 = "#a36936"  #orange


janela = Tk()
janela.title("Calculator")
janela.geometry("235x318")
janela.config(background=cor1)

frame_tela = Frame(janela, width=235, height=50, background=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando botôes

b_1 = Button(frame_corpo, text="C", width=11, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=5, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text="/", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text="7", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=59, y=52)

b_5 = Button(frame_corpo, text="8", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=52)

b_6 = Button(frame_corpo, text="9", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, text="*", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)


b_8 = Button(frame_corpo, text="7", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)

b_9 = Button(frame_corpo, text="8", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=52)

b_10 = Button(frame_corpo, text="9", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=52)

b_11 = Button(frame_corpo, text="*", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=52)



b_12 = Button(frame_corpo, text="C", width=11, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=0)

b_13 = Button(frame_corpo, text="%", width=5, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=118, y=0)

b_14 = Button(frame_corpo, text="/", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=177, y=0)

b_15 = Button(frame_corpo, text="7", width=5, height=2, background=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=59, y=52)

janela.mainloop()


