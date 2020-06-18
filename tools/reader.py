"""Reader files.

This module contains the actions that perform the
readings towards the csv files.
"""
from os import path
import csv
import config
from tools.tools import clear_vector, get_clear_vector_info

# Documents data


class Reader(object):
    """Reader class.

    This class implements the singleton design pattern,
    and contains all the methods for querying csv files.
    """

    __instance = None

    def __new__(cls):
        if Reader.__instance is None:
            Reader.file_exists([
                config.CONFIRMED_CASES_PATH,
                config.DEATHS_CASES_PATH,
                config.RECOVERED_CASES_PATH
            ])
            Reader.__instance = object.__new__(cls)
        
        return Reader.__instance

    def read_file(self, file, _callback, *args):
        """Read a file.
        
        Read a file and execute the _callback function received by parameters,
        passing the obtained data.
        """
        with open(file, 'r') as read_file:
            reader = csv.reader(read_file)
            return _callback(reader, args)

    def get_country_rows(self, file, country):
        """Return data list."""
        def country_rows(reader, country):
            data = []
            for row in reader:
                if row[config.COUNTRY_COLUMN] == country[0]:
                    data.append(row)
            
            return data
        return self.read_file(file, country_rows, country)
        

    def get_first_row(self, file):
        """Return the first row of file."""
        func = lambda reader, args : next(reader)
        return self.read_file(file, func)

    
    def global_info(self):
        # Devuleve 3 arreglos (casos confirmados, recuperados y decesos) de enteros con la información de todos los países del dataset.
        def callback(reader, args):
            """Return confirmed case."""
            data = []
            for row in reader:
                if not row[config.COUNTRY_COLUMN] == 'Country/Region' and not row[config.COUNTRY_COLUMN] == '#country+name':
                    data.append(row)
            return data

        all_confirmed_cases = self.read_file(config.CONFIRMED_CASES_PATH, callback)
        all_recovered_cases = self.read_file(config.RECOVERED_CASES_PATH, callback)
        all_deaths_cases    = self.read_file(config.DEATHS_CASES_PATH, callback)

        all_confirmed_cases, all_recovered_cases, all_deaths_cases = get_clear_vector_info(all_confirmed_cases, all_recovered_cases, all_deaths_cases, self)
        
        return all_confirmed_cases, all_recovered_cases, all_deaths_cases

    @staticmethod
    def file_exists(files_path):
        """Throw an error if it doesn't find a file."""
        for file in files_path:
            if not path.exists(file):
                raise Exception('The file "{}" was not found.'.format(file))
