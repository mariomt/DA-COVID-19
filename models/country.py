"""Country models."""

# LocalModules
from tools.validations import countrys_to_lower
from tools.reader import Reader

confirmed_cases_path = 'Raw data\\time_series_covid19_confirmed_global_iso3_regions.csv'

def show_all_countries():
    """Return the countries name."""
    def callback(reader, args):
        country_names = []
        for vector in reader:
            country_names.append( vector[1] )

        country_names.remove('Country/Region')
        country_names.remove('#country+name')
        country_names = list( dict.fromkeys(country_names) )
        return country_names
    
    reader = Reader( )
    return reader.read_file(confirmed_cases_path, callback)

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
        msg_error = country_name + ' no se encuentra en la lista o no esta escrito correctamente.\n Revise nuestra lista países disponibles. \n' 

        if country_name in lower_countrys:
            position = lower_countrys.index(country_name)
            return Country.countries[position]
        else:
            raise Exception('The country "{}" was not found.'.format(country_name))

    @staticmethod
    def show_all_names():
        """Return the name of countries."""
        return show_all_countries()
    

    def get_confirmed_cases(self):
        """Return the confirmed cases."""
        pass


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

