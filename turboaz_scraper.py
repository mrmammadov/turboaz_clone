import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os

url = 'https://turbo.az'

r = requests.get(url)


# JSON File to hold the data
cars_json = []

if r.status_code == 200:
    html = BeautifulSoup(r.text, 'lxml')
    divs = html.find_all('div', 'products-i')
    for div in divs:
        # Dictionary to hold the individual car details
        cars_dict = {}

        car_profile_url = url + div.a['href']
        car_profile_request = requests.get(car_profile_url)
        if car_profile_request.status_code == 200:
            car_profile_html = BeautifulSoup(car_profile_request.text, 'lxml')
            cars_dict['name'] = car_profile_html.find('h1', 'product-name').text
            cars_dict['price'] = car_profile_html.find('div', 'product-price').text
            ul = car_profile_html.find('ul', 'product-properties')
            li_list = ul.find_all('li')
            cars_dict['city'] = li_list[0].find('div').text
            cars_dict['brand'] = li_list[1].find('div').text
            cars_dict['year'] = li_list[3].find('div').text
            cars_dict['category'] = li_list[4].find('div').text
            cars_dict['color'] = li_list[5].find('div').text
            cars_dict['engine'] = li_list[6].find('div').text

            # Appending into list for turning data into JSON
            cars_json.append(cars_dict)

# JSON conversion
with open(os.getcwd() + '/car_data.json', 'w') as write_file:
    json.dump(cars_json, write_file)