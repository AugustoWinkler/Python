
def despesas_Mensais():
    despesas = despesas_Operacionais/dias_Trabalhados
    return despesas

def hora_Maquina():
    preco_HoraMaquina = (mao_de_Obra()+hora_Laser()+Depreciacao_Anual()+despesas_Mensais())/tempo_Trabalhado()
    return preco_HoraMaquina

def mao_de_Obra():
    tempo = tempo_Trabalhado()
    funcionario = operador/tempo
    return funcionario

def tempo_Trabalhado():
    tempo = dias_Trabalhados * horas_DiasTrabalhados
    return tempo

def hora_Laser(custo_Laser,vida_UtilLaser):
    valor = (custo_Laser/vida_UtilLaser)
    return valor

def Depreciacao_Anual():
    depreciacao = (valor_Maquina - valor_Residual)/vida_UtilMaquina
    return depreciacao

def Calcular_Hora_Maquina():
    hora = 0
    return hora