"""Application main app."""

from flask import Flask, request, jsonify
import requests
import logging, coloredlogs
import os, csv, tablib

app = Flask(__name__, static_url_path='')
coloredlogs.install(level='DEBUG', isatty=True)
logger = logging.getLogger('app_log')

def print_to_csv(data):
        logger.debug(f'printing [{data}] results to CSV file')
        col_names = ['Name', 'Location', 'Image']    
        
        with open(os.path.join(os.getcwd(), "output.csv"), 'w', newline='') as csv_file:
            tsv_output = csv.writer(csv_file)
            tsv_output.writerow(col_names)
            tsv_output.writerows(data) 

@app.route('/')
@app.route('/healthcheck')
def echo_isalive():
    service_name = 'Rick and Morty Service'
    return jsonify('{service_name} is Alive!')

@app.route('/find-live-humans')
def find_live_humans():
    live_humans = []
    api_endpoint = 'https://rickandmortyapi.com/api/character'
    response = requests.get(api_endpoint).json()
    all_characters = response['results']
    logger.debug(all_characters)
    for char in all_characters:
        if char['status'] == 'Alive' and char['species'] == 'Human' and 'Earth' in char['origin']['name']:
            char_details = [char['name'], char['location']['name'], char['image']]
            live_humans.append(char_details)
    logger.debug('Sending all Live Humans found on Earth to a CSV file!')
    logger.debug(f'Live Humans found: {live_humans}')
    print_to_csv(live_humans)
    if not live_humans:
        ret_val = jsonify(results=0, message="No live Humans from Earth found! :-(")
    else:
        ret_val = jsonify(live_humans)
    return(ret_val)

@app.route('/csv')
def show_csv_file():
    dataset = tablib.Dataset()
    with open(os.path.join(os.path.dirname(__file__), 'output.csv')) as f:
        dataset.csv = f.read()
    return jsonify(dataset.dict)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
