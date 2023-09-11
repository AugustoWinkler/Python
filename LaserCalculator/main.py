from tkinter import *
from ttkthemes import ThemedStyle

app = Tk()
app.title("Calculadora Laser")
app.geometry("620x500")
app.configure(background="#dde")
style = ThemedStyle(app)
style.set_theme("black")

# Configuração comum para todos os LabelFrames
label_frame_config = {
    "borderwidth": 1,
    "relief": "solid",
    "labelanchor": N,
    "padx": 10,
    "pady": 10,
}

# Tamanho comum para todos os LabelFrames
frame_width = 300
frame_height = 150

# Variáveis Globais
valor_Maquina = float(0.0)
valor_Residual = float(0.0)
vida_UtilMaquina = float(0.0)
custo_Laser = float(0.0)
vida_UtilLaser = float(0.0)
dias_Trabalhados = float(0.0)
horas_DiasTrabalhados = float(0.0)
despesas_Operacionais = float(0.0)  # Consumo de Energia Elétrica, Custos Manutenção e Reparos, Aluguel, Outros..
operador = float(0.0)

# Sessão da Máquina
maquina = LabelFrame(app, text="Máquina", width=frame_width, height=frame_height, **label_frame_config)
maquina.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

# Preço da Máquina.
maquinavalor = Label(maquina, text="Valor Máquina:")
maquinavalor.grid(row=1, column=1, padx=5, pady=5)
maquinavaloren = Entry(maquina)
maquinavaloren.grid(row=1, column=2, padx=5, pady=5)

# Valor Residual da Máquina.
residualvalor = Label(maquina, text="Valor Residual:")
residualvalor.grid(row=2, column=1, padx=5, pady=5)
residualvaloren = Entry(maquina)
residualvaloren.grid(row=2, column=2, padx=5, pady=5)

# Vida Útil da Máquina.
vidautilmaquina = Label(maquina, text="Vida Útil:")
vidautilmaquina.grid(row=3, column=1, padx=5, pady=5)
vidautilmaquinaen = Entry(maquina)
vidautilmaquinaen.grid(row=3, column=2, padx=5, pady=5)

# Sessão do Laser
laser = LabelFrame(app, text="Laser", width=frame_width, height=frame_height, **label_frame_config)
laser.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

# Valor Laser.
valorlaser = Label(laser, text="Valor Laser:")
valorlaser.grid(row=1, column=1, padx=5, pady=5)
valorlaseren = Entry(laser)
valorlaseren.grid(row=1, column=2, padx=5, pady=5)

# Vida Útil do Laser.
vidalaser = Label(laser, text="Vida Útil:")
vidalaser.grid(row=2, column=1, padx=5, pady=5)
vidalaseren = Entry(laser)
vidalaseren.grid(row=2, column=2, padx=5, pady=5)

# Dias de Trabalho
funcionamento = LabelFrame(app, text="Carga Horária", width=frame_width, height=frame_height, **label_frame_config)
funcionamento.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

# Dias de Trabalho.
diaTrabalho = Label(funcionamento, text="Dias de Trabalho:")
diaTrabalho.grid(row=1, column=1, padx=5, pady=5)
diaTrabalhoen = Entry(funcionamento)
diaTrabalhoen.grid(row=1, column=2, padx=5, pady=5)

# Horas Diárias.
horasDia = Label(funcionamento, text="Horas Diárias:")
horasDia.grid(row=2, column=1, padx=5, pady=5)
horasDiaen = Entry(funcionamento)
horasDiaen.grid(row=2, column=2, padx=5, pady=5)

# Material Custo
material = LabelFrame(app, text="Material", width=frame_width, height=frame_height, **label_frame_config)
material.grid(row=1, column=3, padx=5, pady=5, rowspan=3, columnspan=3, sticky="nsew")

# Material.
tipomaterial = Label(material, text="Material:")
tipomaterial.grid(row=1, column=1, padx=5, pady=5)
tipomaterialen = Entry(material)
tipomaterialen.grid(row=1, column=2, padx=5, pady=5)

# Preço do Material.
valormaterial = Label(material, text="Preço:")
valormaterial.grid(row=2, column=1, padx=5, pady=5)
valormaterialen = Entry(material)
valormaterialen.grid(row=2, column=2, padx=5, pady=5)

# Quantidade de Material.
quantidadematerial = Label(material, text="Quantidade:")
quantidadematerial.grid(row=3, column=1, padx=5, pady=5)
quantidadematerialen = Entry(material)
quantidadematerialen.grid(row=3, column=2, padx=5, pady=5)

# Despesas Operacionais
despesas = LabelFrame(app, text="Despesas Operacionais", width=frame_width, height=frame_height, **label_frame_config)
despesas.grid(row=4, column=3, padx=5, pady=5, rowspan=2, columnspan=2, sticky="nsew")  # Usamos sticky para preencher toda a célula

# Despesas Operacionais.
despesasOperacionais = Label(despesas, text="Despesas Operacionais")
despesasOperacionais.grid(row=1, column=1, padx=5, pady=5)
despesasOperacionaisen = Entry(despesas)
despesasOperacionaisen.grid(row=1, column=2, padx=5, pady=5)

# Custo do Operador.
custoOperador = Label(despesas, text="Custo do Operador")
custoOperador.grid(row=2, column=1, padx=5, pady=5)
custoOperadoren = Entry(despesas)
custoOperadoren.grid(row=2, column=2, padx=5, pady=5)

# Funções
funcoes = LabelFrame(app, text="Funções", width=frame_width, height=frame_height, **label_frame_config)
funcoes.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")

# Adicionar Material
adicionarMat = Button(funcoes, text="Adicionar Material")
adicionarMat.grid(row=1, column=1, pady=5, padx=5)

# Excluir Material
excluirMat = Button(funcoes, text="Excluir Material")
excluirMat.grid(row=1, column=2, padx=5, pady=5)

# Lucro Desejado
lucroDesejado = Label(funcoes, text="Lucro Desejado")
lucroDesejado.grid(row=2, column=1, padx=5, pady=5)
lucroDesejadoen = Entry(funcoes)
lucroDesejadoen.grid(row=2, column=2, padx=5, pady=5)

# Botão calcular
calcularBtn = Button(app, text="Calcular Valor.", width=50, height=2, background="Green")
calcularBtn.grid(row=8, columnspan=4, padx=5, pady=5, sticky="nsew")

# Cálculos
calcular = LabelFrame(app, text="Cálculos", width=frame_width * 2, height=50, **label_frame_config)
calcular.grid(row=9, column=1, columnspan=4, padx=5, pady=5, sticky="nsew")

# Valor Hora Máquina
horaMaquina = Label(calcular, text="Hora Máquina: {}")
horaMaquina.grid(row=1, column=1, padx=5, pady=5)
minutoMaquina = Label(calcular, text="Minuto Máquina: {}")
minutoMaquina.grid(row=1, column=2, padx=5, pady=5)
lucroEstimado = Label(calcular, text="Lucro Estimado: {}R$")
lucroEstimado.grid(row=1, column=3, padx=5, pady=5)
valorTotal = Label(calcular, text="Valor Total: {}")
valorTotal.grid(row=1, column=4, padx=5, pady=5)


# Funções de cálculo e atualização de resultados
def despesas_Mensais():
    despesas = despesas_Operacionais / dias_Trabalhados
    return despesas

def hora_Maquina():
    preco_HoraMaquina = (mao_de_Obra() + hora_Laser() + Depreciacao_Anual() + despesas_Mensais()) / tempo_Trabalhado()
    return preco_HoraMaquina

def mao_de_Obra():
    tempo = tempo_Trabalhado()
    funcionario = operador / tempo
    return funcionario

def tempo_Trabalhado():
    tempo = dias_Trabalhados * horas_DiasTrabalhados
    return tempo

def hora_Laser():
    valor = (custo_Laser / vida_UtilLaser)
    return valor

def Depreciacao_Anual():
    depreciacao = (valor_Maquina - valor_Residual) / vida_UtilMaquina
    return depreciacao

def calcular_valor():
    global valor_Maquina, valor_Residual, vida_UtilMaquina, custo_Laser, vida_UtilLaser, dias_Trabalhados, horas_DiasTrabalhados, despesas_Operacionais, operador

    valor_Maquina = float(maquinavaloren.get())
    valor_Residual = float(residualvaloren.get())
    vida_UtilMaquina = float(vidautilmaquinaen.get())
    custo_Laser = float(valorlaseren.get())
    vida_UtilLaser = float(vidalaseren.get())
    dias_Trabalhados = float(diaTrabalhoen.get())
    horas_DiasTrabalhados = float(horasDiaen.get())
    despesas_Operacionais = float(despesasOperacionaisen.get())
    operador = float(custoOperadoren.get())

    # Chame as funções de cálculo
    despesas_mensais = despesas_Mensais()
    preco_hora_maquina = hora_Maquina()
    # Outras funções de cálculo aqui

    # Exiba os resultados na interface gráfica
    horaMaquina.config(text=f'Hora Máquina: {preco_hora_maquina:.2f}R$')
    # Exiba outros resultados da mesma maneira

# Associe a função ao botão "Calcular Valor"
calcularBtn.config(command=calcular_valor)

app.mainloop()
