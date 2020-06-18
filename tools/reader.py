"""Reader files."""
from os import path
import csv

# Documents data
CONFIRMED_CASES_PATH = 'Raw data\\time_series_covid19_confirmed_global_iso3_regions.csv'
DEATHS_CASES_PATH    = 'Raw data\\time_series_covid19_deaths_global_iso3_regions.csv'
RECOVERED_CASES_PATH = 'Raw data\\time_series_covid19_recovered_global_iso3_regions.csv'

COUNTRY_COLUMN = 1

class Reader(object):
    """Reader class."""

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
                

    @staticmethod
    def file_exists(files_path):
    # Verifica que exista el archivo en la ruta proporsionada.
    # files_path: Es un arreglo de string que contiene rutas de archivos.
        for file in files_path:
            if not path.exists(file):
                raise Exception('The file "{}" was not found.'.format(file))


