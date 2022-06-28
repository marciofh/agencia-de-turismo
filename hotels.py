import requests

#LOCALIZAÇÃO
def getLocationId(location):
	url = "https://travel-advisor.p.rapidapi.com/locations/search"

	querystring = {
		"query": location,
		"limit":"1", #numero de itens por resposta
		"offset":"0",
		"units":"km",
		"location_id":"1",
		"currency":"BRL",
		"sort":"relevance",
		"lang":"pt_BR"
	}

	headers = {
		"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
		"X-RapidAPI-Key": "12bb9c7718mshe8cbe79cbc0f70cp10b4c1jsnfb9d6a4ccc43"  #TOKEN
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	response = response.json()
	
	location_id = response['data'][0]['result_object']['location_id']
	location_string = response['data'][0]['result_object']['location_string']
	img_city = response['data'][0]['result_object']['photo']['images']['small']['url']
	geo_description =response['data'][0]['result_object']['geo_description']
	print('\n' + location_string + '\n' + img_city + '\n' + geo_description + '\n')
	
	getHotels(location_id)


#HOTEIS
def getHotels(location_id):
	url = "https://travel-advisor.p.rapidapi.com/hotels/list"
	limit = 5 #quatidade de hoteis

	nAdults = input("Qtde de Adultos: ")
	nRoomns = input("Qtde de quartos: ")
	nNights = input("Quantas noites: ")

	querystring = {
		"location_id": location_id,
		"adults": nAdults,
		"rooms": nRoomns,
		"nights": nNights,
		"offset":"0",
		"currency":"BRL",
		"order":"asc",
		"limit": limit,
		"sort":"recommended",
		"lang":"pt_BR"
	}

	headers = {
		"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
		"X-RapidAPI-Key": "12bb9c7718mshe8cbe79cbc0f70cp10b4c1jsnfb9d6a4ccc43" #TOKEN
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	response = response.json()

	print("\n--------Principais Hoteis----------------\n")
	for i in range(limit):

		hotel_name = response['data'][i]['name']
		hotel_img = response['data'][i]['photo']['images']['small']['url']
		hotel_rating = response['data'][i]['rating']
		hotel_price = response['data'][i]['price']
		print('\n' + hotel_name + '\n' + hotel_img + '\n' + hotel_rating + '\n' + hotel_price + '\n')

#MAIN
if __name__ == '__main__':
	location = input("Digite o lugar para viajar: ")
	getLocationId(location)