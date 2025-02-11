"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_collection = []

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            neo_collection.append(NearEarthObject(**elem))
    return neo_collection


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    app_collection = []

    with open(cad_json_path, 'r') as infile:
        reader = json.load(infile)
        column_list = reader['fields']
        data = reader['data']
        for i in range(len(data)):
            app_collection.append(CloseApproach(**dict(zip(column_list, data[i]))))
    return app_collection

