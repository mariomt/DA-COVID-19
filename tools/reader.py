"""Reader files.

This module contains the actions that perform the
readings towards the csv files.
"""
from os import path
import csv
from tools.tools import clear_vector, get_clear_vector_info

# Documents data
CONFIRMED_CASES_PATH = 'Raw data\\time_series_covid19_confirmed_global_iso3_regions.csv'
DEATHS_CASES_PATH    = 'Raw data\\time_series_covid19_deaths_global_iso3_regions.csv'
RECOVERED_CASES_PATH = 'Raw data\\time_series_covid19_recovered_global_iso3_regions.csv'

COUNTRY_COLUMN = 1

class Reader(object):
    """Reader class.

    This class implements the singleton design pattern,
    and contains all the methods for querying csv files.
    """

    __instance = None

    def __new__(cls):
        if Reader.__instance is None:
            Reader.file_exists([
                CONFIRMED_CASES_PATH,
                DEATHS_CASES_PATH,
                RECOVERED_CASES_PATH
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
                if row[COUNTRY_COLUMN] == country[0]:
                    data.append(row)
            
            return data
        return self.read_file(file, country_rows, country)
        

    def get_first_row(self, file):
        """Return the first row of file."""
        func = lambda reader, args : next(reader)
        return self.read_file(file, func)

    def get_info_by_country_name(self, country):
    # Devuelve 3 arreglos (casos confirmados, recuperados y decesos) de tipo string con la 
    # información completa de un pais dado.
    # country: Es el nombre de un pais dado por el usuario (string).

        raw_confirmed_cases = self.get_country_rows(CONFIRMED_CASES_PATH, country)
        raw_recovered_cases = self.get_country_rows(RECOVERED_CASES_PATH, country)
        raw_deaths_cases = self.get_country_rows(DEATHS_CASES_PATH, country)
        return raw_confirmed_cases, raw_recovered_cases, raw_deaths_cases

    
    def global_info(self):
        # Devuleve 3 arreglos (casos confirmados, recuperados y decesos) de enteros con la información de todos los países del dataset.
        def callback(reader, args):
            """Return confirmed case."""
            data = []
            for row in reader:
                if not row[COUNTRY_COLUMN] == 'Country/Region' and not row[COUNTRY_COLUMN] == '#country+name':
                    data.append(row)
            return data

        all_confirmed_cases = self.read_file(CONFIRMED_CASES_PATH, callback)
        all_recovered_cases = self.read_file(RECOVERED_CASES_PATH, callback)
        all_deaths_cases    = self.read_file(DEATHS_CASES_PATH, callback)

        all_confirmed_cases, all_recovered_cases, all_deaths_cases = get_clear_vector_info(all_confirmed_cases, all_recovered_cases, all_deaths_cases, self)
        
        return all_confirmed_cases, all_recovered_cases, all_deaths_cases


    def get_recovered_cases(self, country_name):
    # Devuelve un arreglo de enteros con la información de los casos recuperados de un país.
    # country_name: Es el nomnre del país.
        def callback(reader, args):
            data = []
            for row in reader:
                if row[COUNTRY_COLUMN] == country_name:
                    data.append(row)
            return data

        recovered_cases = self.read_file(RECOVERED_CASES_PATH,callback)

        recovered_cases = clear_vector(recovered_cases, self)
        return recovered_cases

    def get_confirmed_cases(self, country_name):
    # Devuleve un arreglo de enteros que contiene la información sobre los casos confirmados de un país.
    # country_name: Es el nombre del pais.
        def callback(reader, args):
            data = []
            for row in reader:
                if row[COUNTRY_COLUMN] == country_name:
                    data.append(row)
            return data

        confirmed_cases = self.read_file(CONFIRMED_CASES_PATH, callback)
        confirmed_cases = clear_vector(confirmed_cases, self)
        return confirmed_cases
                

    def get_deaths_cases(self, country_name):
    # Devuelve un arreglo de enteros con la información de los decesos de un país.
    # country_name: Es el nombre del país.
        def callback(reader, args):
            data = []
            for row in reader:
                if row[COUNTRY_COLUMN] == country_name:
                    data.append(row)
            return data

        deaths_cases = self.read_file(DEATHS_CASES_PATH, callback)

        deaths_cases = clear_vector(deaths_cases, self)
        return deaths_cases

    @staticmethod
    def file_exists(files_path):
        """Throw an error if it doesn't find a file."""
        for file in files_path:
            if not path.exists(file):
                raise Exception('The file "{}" was not found.'.format(file))
