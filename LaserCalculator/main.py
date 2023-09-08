#Calculadora de Custo Hora CNC Laser +  Materials

from modulos import *


valor_Maquina = float(3000)
valor_Residual = float(0)
vida_UtilMaquina = int(10)
custo_Laser = float(3000)
vida_UtilLaser = int(8000)
dias_Trabalhados = int(20)
horas_DiasTrabalhados = int(8)
despesas_Operacionais = float(200) #Consumo de Energia Elétrica,Custos Manutenção e Reparos,Aluguel, Outros..
operador = float(2000)



print(f"{teste(despesas_Operacionais,dias_Trabalhados):.2f}R$")
print(hora_Laser(vida_UtilLaser,vida_UtilLaser))