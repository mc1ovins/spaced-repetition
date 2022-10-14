'''
2 Sep 2022
Axel Daniel Padilla Reyes

This file contains functions to interact with the database.
'''
import yaml
from yaml.loader import SafeLoader
import os


def load_db(db_name):
    """
    This function loads the database from the file
    and returns it as a dictionary.
    """
    with open(os.path.join(os.getcwd(), 'db', db_name)) as f:
        return yaml.load(f, Loader=SafeLoader)


def write_db(db, db_name):
    """
    This function overwrites the database with the
    dictionary passed as an argument.
    """
    with open(os.path.join(os.getcwd(), 'db', db_name), 'w') as f:
        yaml.dump(db, f, indent=4, default_flow_style=False)
