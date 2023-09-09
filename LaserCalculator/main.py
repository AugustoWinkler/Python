#Calculadora de Custo Hora CNC Laser +  Materials

from modulos import *
from tkinter import *

app=Tk()
app.title("Calculadora Laser")
app.geometry("720x486")
app.configure(background="#dde")


#Sessão da Máquina
maquina = LabelFrame(app, text="Máquina", borderwidth=1,relief="solid",width=350,height=150).grid(row=1,column=1,columnspan=2,rowspan=3)
#Preço da Máquina.
maquinavalor = Label(maquina, text="Valor Máquina:").grid(row=1,column=1)
maquinavaloren = Entry(maquina).grid(row=1,column=2)
#Valor Residual da Máquina.
residualvalor = Label(maquina, text="Valor Residual::").grid(row=2,column=1)
residualvaloren = Entry(maquina).grid(row=2,column=2)
#Vida Util da Máquina.
vidautilmaquina = Label(maquina, text="Valor Máquina:").grid(row=3,column=1)
vidautilmaquinaen = Entry(maquina).grid(row=3,column=2)


#Sessão do Laser
laser = LabelFrame(app,text="Laser", borderwidth=1, relief="solid", width=350, height=150).place(y=200)
valorlaser = Label(laser, text="Laser").grid(row=1,column=1)
valorlaseren = Entry().grid(row=1,column=2)



valor_Maquina = float(3000)
valor_Residual = float(0)
vida_UtilMaquina = int(10)
custo_Laser = float(3000)
vida_UtilLaser = int(8000)
dias_Trabalhados = int(20)
horas_DiasTrabalhados = int(8)
despesas_Operacionais = float(200) #Consumo de Energia Elétrica,Custos Manutenção e Reparos,Aluguel, Outros..
operador = float(2000)

app.mainloop()


