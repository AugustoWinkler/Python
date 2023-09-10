from modulos import *
from tkinter import *

app = Tk()
app.title("Calculadora Laser")
app.geometry("720x486")
app.configure(background="#dde")

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

# Sessão da Máquina
maquina = LabelFrame(app, text="Máquina", width=frame_width, height=frame_height, **label_frame_config)
maquina.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")  # Usamos sticky para preencher toda a célula

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
laser.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")  # Usamos sticky para preencher toda a célula

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
funcionamento.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")  # Usamos sticky para preencher toda a célula

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
material.grid(row=1, column=3, padx=5, pady=5, rowspan=3, columnspan=3, sticky="nsew")  # Usamos sticky para preencher toda a célula

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

# Restante do seu código

app.mainloop()
