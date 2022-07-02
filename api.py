import requests
from datetime import datetime
from credentials import keys
import json

TOKEN = keys.get('TOKEN')

class Api:
    def get_locationId(location):
        url = "https://travel-advisor.p.rapidapi.com/locations/search"

        querystring = {
            "query": location,
            "limit":"1",
            "offset":"0",
            "units":"km",
            "location_id":"1",
            "currency":"BRL",
            "sort":"relevance",
            "lang":"pt_BR"
        }
        headers = {
            "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
            "X-RapidAPI-Key": TOKEN
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        location_id = response['data'][0]['result_object']['location_id']
        
        return location_id

    def get_hotels(location_id, passageiros, data_ida, data_volta):
        url = "https://travel-advisor.p.rapidapi.com/hotels/get-details"

        data_ida = datetime.strptime(data_ida, "%Y-%m-%d").date()
        data_volta = datetime.strptime(data_volta, "%Y-%m-%d").date()
        noites = (data_volta - data_ida).days

        querystring = {
            "location_id": location_id,
            "checkin": data_ida,
            "adults": passageiros,
            "lang":"pt_BR",
            "currency":"BRL",
            "nights": noites
        }   
        headers = {
            "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
            "X-RapidAPI-Key": TOKEN
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        dados = (response['data'])

        hotels = []
        for i in range(5):
            dados[i]['raw_ranking'] = float(dados[i]['raw_ranking'])
            dados[i]['raw_ranking'] = round(dados[i]['raw_ranking'], 2)

            hotels.append({
                "nome" : dados[i]['name'],
                "preco" : dados[i]['price'],
                "foto" : dados[i]['photo']['images']['small']['url'],
                "ranking_site" : dados[i]['raw_ranking'],
                "stars": dados[i]['hotel_class'],
                "url_site" : dados[i]['web_url'],
                "endereco" : dados[i]['address'] 
            })

        return hotels
