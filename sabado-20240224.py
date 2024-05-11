import folium
import os
import requests


def geocode(address):
    url = 'https://photon.komoot.io/api/?q={}-$limit=1'.format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data['features']) > 0:
            coordinates = data['features'][0]['geometry']['coordinates']
            return coordinates[::-1]
    return None


def create_map(latitude, longitude):
    mapa = folium.Map(location=[latitude, longitude], zoom_start=15)
    marker = folium.Marker([latitude, longitude], popup='Endereço').add_to(mapa)
    marker.add_to(mapa)
    return mapa


endereco = input("Digite o endereço: ")
coords = geocode(endereco)
if coords:
    latitude, longitude = coords
    mapa = create_map(latitude, longitude)
    diretorio = input("Digite o diretório onde deseja salvar o mapa: ")

    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    nome_arquivo = input("Digite o nome do arquivo: ")
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    mapa.save(caminho_arquivo)
    print(f"Mapa salvo em {caminho_arquivo}")
else:
    print("O diretório informado não existe")
