# Implementa uma interface usando Tkinter para previsão do tempo

import requests
import tkinter as tk

# Janela principal
root = tk.Tk()

# Título da janela
root.title("Previsão do Tempo")

# Largura e altura da janela
root.geometry("400x600")

# Label da caixa de entrada de texto
label = tk.Label(root, text="Digite a cidade", font=("Helvetica", 16), width=30)

# Posiciona o label na janela
label.grid(row=0, column=0, padx=10, pady=10)

# Entrada de texto para digitar a cidade
city = tk.Entry(root, font=("Helvetica", 16), justify="center", width=30)

# Posiciona a entrada de texto na janela
city.grid(row=1, column=0, padx=10, pady=10)

# Função para buscar a previsão do tempo
def get_weather(city):
    # Cria um Label para mostrar a previsão do tempo
    today_weather_label = tk.Label(root, text="Hoje: NÃO IMPLEMENTADO!", font=("Helvetica", 16), justify="left")
    tomorrow_weather_label = tk.Label(root, text="Amanhã: NÃO IMPLEMENTADO!", font=("Helvetica", 16), justify="left")

    # Posiciona o label na janela
    today_weather_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
    tomorrow_weather_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Botão para buscar a previsão do tempo
get_weather_btn = tk.Button(root, text="Buscar Previsão do Tempo", command=lambda: get_weather(city.get()))

# Posiciona o botão na janela
get_weather_btn.grid(row=2, column=0, padx=10, pady=10)

# Label para mostrar a previsão do tempo
weather_label = tk.Label(root, text="Previsão do Tempo")

# Posiciona o label na janela
weather_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)




# Finaliza a janela
root.mainloop()