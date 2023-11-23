from tkinter import *
from tkinter import ttk

#Cores
preto = '#1e1f1e'
branco = '#feffff'
azul = '#38576b'
cinza = '#ECEFF1'
laranja = '#FFAB40'

#Janela
janela = Tk()
janela.title('Claculadora')
janela.geometry('235x310')
janela.config(bg=preto)

#Frames

frame_tela = Frame(janela, width=235, height=50, bg=azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


valores = ''
valor_texto = StringVar()


#Funções de entradaaa de valores
def entrar_valores(event):
    global valores
    valores = valores + str(event)

    #Passando valor para a tela
    valor_texto.set(valores)

#Função para clacular

def calcular():
    global valores
    resultado = eval(valores)
    valor_texto.set(str(resultado))



def limpar_tela():
    global valores
    valores = ''
    valor_texto.set('')



#Label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=azul, fg=branco)
app_label.place(x=0, y=0)


#Botões

limpar = Button(frame_corpo, command=limpar_tela,text='C', width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
limpar.place(x=0, y=0)
porcentagem = Button(frame_corpo, command=lambda: entrar_valores('%'), text='Resto', width=5, height=2, bg=cinza,  font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
porcentagem.place(x=118, y=0)
dividir = Button(frame_corpo, command=lambda: entrar_valores('/'),text='/', width=5, height=2, bg=laranja, fg=branco,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
dividir.place(x=177, y=0)

botao_7 = Button(frame_corpo, command=lambda: entrar_valores('7'),text='7', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=0, y=52)
botao_8 = Button(frame_corpo, command=lambda: entrar_valores('8'),text='8', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=59, y=52)
botao_9 = Button(frame_corpo, command=lambda: entrar_valores('9'),text='9', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=118, y=52)
multiplicar = Button(frame_corpo, command=lambda: entrar_valores('*'),text='*', width=5, height=2, bg=laranja, fg=branco,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
multiplicar.place(x=177, y=52)

botao_4 = Button(frame_corpo, command=lambda: entrar_valores('4'),text='4', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=0, y=104)
botao_5 = Button(frame_corpo, command=lambda: entrar_valores('5'),text='5', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=59, y=104)
botao_6 = Button(frame_corpo, command=lambda: entrar_valores('6'),text='6', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=118, y=104)
subtrair = Button(frame_corpo, command=lambda: entrar_valores('-'),text='-', width=5, height=2, bg=laranja, fg=branco,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
subtrair.place(x=177, y=104)

botao_1 = Button(frame_corpo, command=lambda: entrar_valores('1'),text='1', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=156)
botao_2 = Button(frame_corpo, command=lambda: entrar_valores('2'),text='2', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=59, y=156)
botao_3 = Button(frame_corpo, command=lambda: entrar_valores('3'),text='3', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=118, y=156)
somar = Button(frame_corpo, command=lambda: entrar_valores('+'),text='+', width=5, height=2, bg=laranja, fg=branco,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
somar.place(x=177, y=156)

botao_0 = Button(frame_corpo, command=lambda: entrar_valores('0'),text='0', width=11, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_0.place(x=0, y=208)
ponto = Button(frame_corpo, command=lambda: entrar_valores('.'),text='.', width=5, height=2, bg=cinza,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
ponto.place(x=118, y=208)
igual = Button(frame_corpo, command=calcular,text='=', width=5, height=2, bg=laranja, fg=branco,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
igual.place(x=177, y=208)




janela.mainloop()