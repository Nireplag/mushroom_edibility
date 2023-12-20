import requests


#url = 'http://localhost:9696/predict' # localhost test
url = 'https://mushroom-edibility-2rtrkbrwna-uc.a.run.app/predict' # GCP deployment

mushroom = {
    "cap_shape": 'x',
    "cap_surface": 'y',
    "cap_color": 'n',
    "bruises": 't',
    "odor": 'n',
    "gill_spacing": 'c',
    "gill_size": 'b',
    "gill_color": 'e',
    "stalk_root": '?',
    "stalk_surface_above_ring":'s',
    "stalk_surface_below_ring":'s',
    "stalk_color_above_ring":'e',
    "stalk_color_below_ring":'e',
    "veil_color":'w',
    "ring_number":'t',
    "ring_type":'e',
    "spore_print_color":'w',
    "population":'c',
    "habitat":'w'
}


response = requests.post(url, json=mushroom).json()
print(response) # expect output 0


mushroom = {
    "cap_shape": 'k',
    "cap_surface": 'y',
    "cap_color": 'n',
    "bruises": 'f',
    "odor": 'f',
    "gill_spacing": 'c',
    "gill_size": 'n',
    "gill_color": 'b',
    "stalk_root": '?',
    "stalk_surface_above_ring":'s',
    "stalk_surface_below_ring":'k',
    "stalk_color_above_ring":'w',
    "stalk_color_below_ring":'w',
    "veil_color":'w',
    "ring_number":'o',
    "ring_type":'e',
    "spore_print_color":'w',
    "population":'v',
    "habitat":'l'
}

response = requests.post(url, json=mushroom).json()
print(response) # expect output 1
