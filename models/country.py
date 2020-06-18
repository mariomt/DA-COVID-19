"""Country models."""

# LocalModules
from tools.validations import countrys_to_lower
from tools.tools import clear_vector
from tools.reader import Reader
import config


def show_all_countries():
    """Return the countries name."""
    def callback(reader, args):
        country_names = []
        for vector in reader:
            country_names.append( vector[config.COUNTRY_COLUMN] )

        country_names.remove('Country/Region')
        country_names.remove('#country+name')
        country_names = list( dict.fromkeys(country_names) )
        return country_names
    
    reader = Reader( )
    return reader.read_file(config.CONFIRMED_CASES_PATH, callback)

class Country(object):
    """Country model.

    This model contains the characteristics and functionalities
    that a country should contain.
    """

    countries = show_all_countries()

    def __init__(self, name, **kwargs):
        """Init method."""
        self.name = Country.country_validation(name);
        self.first_confirmed_infected = '2000-01-01' if 'first_confirmed_infected' not in kwargs else kwargs.get('first_confirmed_infected')
        self.confirmed_infected_accumulated = 0 if 'confirmed_infected_accumulated' not in kwargs else kwargs.get('confirmed_infected_accumulated')
        self.currently_infected = 0 if 'currently_infected' not in kwargs else kwargs.get('currently_infected')
        self.cumulative_recoveries = 0 if 'cumulative_recoveries' not in kwargs else kwargs.get('cumulative_recoveries')
        self.cumulative_deaths = 0 if 'cumulative_deaths' not in kwargs else kwargs.get('cumulative_deaths')            
        self.mortality_rate = 0 if 'mortality_rate' not in kwargs else kwargs.get('mortality_rate')
        self.recovery_rate = 0 if 'recovery_rate' not in kwargs else kwargs.get('recovery_rate')
        self.active_infection_rate = 0 if 'active_infection_rate' not in kwargs else kwargs.get('active_infection_rate')

    @staticmethod
    def country_validation(name):
        country_name = name.lower().strip()
        lower_countrys = countrys_to_lower(Country.countries)

        if country_name in lower_countrys:
            position = lower_countrys.index(country_name)
            return Country.countries[position]
        else:
            raise NotFoundError('The country "{}" was not found.'.format(name))

    @staticmethod
    def show_all_names():
        """Return the name of countries."""
        return show_all_countries()
    

    def get_confirmed_cases(self):
        """Return the confirmed cases."""
        pass

    def get_data_info(self):
    # Devuelve 3 arreglos (casos confirmados, recuperados y decesos) de tipo string con la 
    # información completa de un pais dado.
    # country: Es el nombre de un pais dado por el usuario (string).
        reader = Reader()
        raw_confirmed_cases = reader.get_country_rows(config.CONFIRMED_CASES_PATH, self.name)
        raw_recovered_cases = reader.get_country_rows(config.RECOVERED_CASES_PATH, self.name)
        raw_deaths_cases = reader.get_country_rows(config.DEATHS_CASES_PATH, self.name)
        return raw_confirmed_cases, raw_recovered_cases, raw_deaths_cases

    def get_confirmed_cases(self):
    # Devuleve un arreglo de enteros que contiene la información sobre los casos confirmados de un país.
    # country_name: Es el nombre del pais.
        def callback(reader, args):
            data = []
            for row in reader:
                if row[config.COUNTRY_COLUMN] == self.name:
                    data.append(row)
            return data

        reader = Reader()
        confirmed_cases = reader.read_file(config.CONFIRMED_CASES_PATH, callback)
        confirmed_cases = clear_vector(confirmed_cases, reader)
        return confirmed_cases

    def get_recovered_cases(self):
    # Devuelve un arreglo de enteros con la información de los casos recuperados de un país.
    # country_name: Es el nomnre del país.
        def callback(reader, args):
            data = []
            for row in reader:
                if row[config.COUNTRY_COLUMN] == self.name:
                    data.append(row)
            return data

        reader = Reader()
        recovered_cases = reader.read_file(config.RECOVERED_CASES_PATH,callback)
        recovered_cases = clear_vector(recovered_cases, reader)

        return recovered_cases

    def get_deaths_cases(self):
    # Devuelve un arreglo de enteros con la información de los decesos de un país.
    # country_name: Es el nombre del país.
        def callback(reader, args):
            data = []
            for row in reader:
                if row[config.COUNTRY_COLUMN] == self.name:
                    data.append(row)
            return data

        reader = Reader()
        deaths_cases = reader.read_file(config.DEATHS_CASES_PATH, callback)
        deaths_cases = clear_vector(deaths_cases, reader)
        return deaths_cases


    def str_format(self):
        """Return the object in string format."""
        return """\n--- ---  {}  --- ---
Primer caso confirmado: ' {} 
Casos confirmados acumulados: {:,}     
Casos activos actualmente: -> {:,}       
Casos recuperados acumulados: {:,}    
Decesos acumulados: --------> {:,}    
Indice de mortalidad: ------> {}%
Indice de recuperación: ----> {}%
Indice de casos activos: ---> {}%""".format(
                self.name,
                self.first_confirmed_infected,
                self.confirmed_infected_accumulated,
                self.currently_infected,
                self.cumulative_recoveries,
                self.cumulative_deaths,
                self.mortality_rate,
                self.recovery_rate,
                self.active_infection_rate
            )


class NotFoundError(Exception):
    pass