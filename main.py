#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
import json
import requests

astro_adr = 'http://api.open-notify.org/astros.json'

def main():
    print('Retrieving data from: ', astro_adr)
    raw_astronaut_data = urllib.request.urlopen(astro_adr).read()
    print('Raw data: ', raw_astronaut_data)
    converted_astronaut_data = json.loads(raw_astronaut_data)
    print('Converted data: ', converted_astronaut_data)
    temp_guy = requests.get(astro_adr).json()
    print('Converted MKII data: ', temp_guy)