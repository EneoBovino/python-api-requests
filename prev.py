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

# Função que transforma um nome de cidade ou local em coordenadas geográficas
def get_geocode(city: str):
    # URL da API de geocode
    url = 'https://geocode.maps.co/search?q={nome_do_lugar}&api_key={api_key}'

    # Chave da API
    api_key = '65c3e42a1ba9e761698287tbg28a5a8'

    # Chamando a API de geocode
    response = requests.get(url=url.format(nome_do_lugar=city, api_key=api_key))

    latitude = response.json()[0]['lat']
    longitude = response.json()[0]['lon']

    return {'latitude':latitude, 'longitude':longitude}

# Função que chama a API de previsão do tempo
def call_weather_api(city: str):
    # Chama a API de Geocode para buscar a coodenadas
    geocode = get_geocode(city)

    # Chave da API de previsão do tempo
    api_key = '6fb849316852c21d7964a8a6564e9079'

    # URL da API de previsão do tempo
    url_forecast = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={chave_api}&units=metric&lang=pt_br'

    # Chamando a API de previsão do tempo
    response = requests.get(url=url_forecast.format(lat=geocode['latitude'], lon=geocode['longitude'], chave_api=api_key))

    # Extraindo a lista de previsões do tempo
    forecast_list = response.json()['list']

    # Extraindo e guardando o nome da cidade da previsão retornada
    nome_da_cidade = response.json()['city']['name']

    # Lista com as informações relevantes a serem exibidas na tela
    forecast_data = []
    
    # Iterar sobre a lista de previsões somente nos 5 primeiros resultados
    for forecast in forecast_list[:5]:
        # Data e hora do período da previsão
        datahora = forecast['dt_txt']

        # Temperatura mínima do período
        temp_min = forecast['main']['temp_min']

        # Temperatura máxima do período
        temp_max = forecast['main']['temp_max']

        # Descrição do período
        description = forecast['weather'][0]['description']

        forecast_data.append(
            {
                'nome_da_cidade': nome_da_cidade,
                'datahora': datahora,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'description': description
            }
        )

    return forecast_data

        

# Função para buscar a previsão do tempo
def get_weather(city):
    # Limpa o frame da previsão do tempo
    for widget in weather_frame.winfo_children():
        widget.destroy()

    # Limpa o label da cidade
    city_label.config(text="")

    # Chama a API de previsão
    forecast_data = call_weather_api(city)

    # Coloca o nome da cidade no label
    city_label.config(text=forecast_data[0]['nome_da_cidade'])

    # Itera sobre os dados de previsão e adiciona no frame
    for forecast in forecast_data:
        label_text = forecast['datahora']
        label_text += ' ' + str(forecast['temp_min'])
        label_text += ' ' + str(forecast['temp_max'])
        label_text += ' ' + forecast['description']
        # Cria um Label para mostrar a data e hora, temperatura mínima, temperatura máxima e descrição do tempo no frame da previsão do tempo
        weather_label = tk.Label(
            weather_frame,
            text=label_text,
            font=("Helvetica", 12),
            justify="left"
        )

        weather_label.pack(pady=10)

    

# Botão para buscar a previsão do tempo
get_weather_btn = tk.Button(root, text="Buscar Previsão do Tempo", command=lambda: get_weather(city.get()))

# Posiciona o botão na janela
get_weather_btn.grid(row=2, column=0, padx=10, pady=10)

# Label para mostrar a previsão do tempo
weather_label = tk.Label(root, text="Previsão do Tempo")

# Posiciona o label na janela
weather_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label para mostrar o nome da cidade
city_label = tk.Label(root, text="", font=("Helvetica", 16))

# Posiciona o label na janela
city_label.grid(row=4, column=0, padx=10, pady=10)

# Cria um frame para mostrar a previsão do tempo
weather_frame = tk.Frame(root)

# Posiciona o frame na janela
weather_frame.grid(row=5, column=0, padx=10, pady=10)



# Finaliza a janela
root.mainloop()