from tkinter import Button, Entry, Label, Tk



janela = Tk()


janela.title('Lingotes De Graça')



lb1 = Label(janela,text='login: ')
titulo = Label(janela,text='Insira seu login e senha do Natuto Online ')
lb2 = Label(janela,text='senha: ')

titulo.config(font=("Courier", 20))

ed1 = Entry(janela,)
ed2 = Entry(janela,)

bt1 = Button(janela, text='Confirmar')

titulo.grid(row=0,column=1 )
lb1.grid(row=1, column=0)
lb2.grid(row=2, column=0)

ed1.grid(row=1, column=1)
ed2.grid(row=2, column=1)
bt1.grid(row=3, column=1)
#LxA+
janela.geometry ()

janela.mainloop()


#dsfdsvdsdsffdsf
