from matplotlib import pyplot as plot
from matplotlib import dates as plot_dates
from datetime import date
import Tools

plot.style.use('seaborn') # Estilo de grafica

def show_all_country_info(dates_array, confirmed_cases, recovered_cases, deaths_cases, country_name):
    # Devuelve una grafica con los casos confirmados, recuperados y decesos de COVID-19 de un 
    # país dado por el usuairo.
    # dates_array: Es un arreglo de fechas de tipo date
    # confirmed_cases: Es un arreglo de enteros que contiene la información de los casos confirmados
    # recovered_cases: Es un arreglo de enteros que contiene la información de los casos recuperados
    # deaths_cases: Es un arreglo de enteros que contiene la información de los decesos
    active_cases = get_active_cases(confirmed_cases, recovered_cases, deaths_cases)

    # Graficación de información
    plot.plot(dates_array, confirmed_cases, linestyle='solid', color='red', label='Confirmados')
    plot.plot(dates_array, recovered_cases, linestyle='solid', color='green', label='Recuperados')
    plot.plot(dates_array, deaths_cases, linestyle='solid', color='black', label='Muertes')
    plot.plot(dates_array, active_cases, linestyle='solid', color='yellow', label='Activos')

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento general de COVID-19 en ' + country_name + ' hasta el ' + str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos')
    plot.tight_layout()
    plot.show()

def get_active_cases(confirmed_cases, recovered_cases, deaths_cases):
    array_size = len(confirmed_cases)
    active_cases = []
    
    for n in range(array_size):
        active_cases.append(confirmed_cases[n] - (recovered_cases[n] + deaths_cases[n]))
    
    return active_cases

def show_country_confirmed_cases(dates_array, confirmed_cases, country_name):
    plot.plot(dates_array, confirmed_cases, linestyle='solid', color='red', label='Casos confirmados')

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos confirmados de COVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos confirmados')
    plot.tight_layout()
    plot.show()

def show_country_recovered_cases(dates_array, recovered_cases, country_name):
    plot.plot(dates_array, recovered_cases, linestyle='solid', color='green', label='Casos recuperados')

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos recuperados de COVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos recuperados')
    plot.tight_layout()
    plot.show()

def show_country_deaths_cases(dates_array, deaths_cases, country_name):
    plot.plot(dates_array, deaths_cases, linestyle='solid', color='black', label='Decesos')

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de los decesos por deCOVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de decesos')
    plot.tight_layout()
    plot.show()

def show_country_active_cases(dates_array, confirmed_cases, recovered_cases, deaths_cases, country_name):
    active_cases = get_active_cases(confirmed_cases, recovered_cases, deaths_cases)
    plot.plot(dates_array, active_cases, linestyle='solid', color='yellow', label='Casos activos')

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos activos de COVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos activos')
    plot.tight_layout()
    plot.show()

def show_confirmed_vs_countrys(dates_array, confirmed_first_country, confirmed_second_country, first_name, second_name):
    plot.plot(dates_array, confirmed_first_country, linestyle='solid', color='blue', label=first_name)
    plot.plot(dates_array, confirmed_second_country, linestyle='solid', color='green', label=second_name)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos confirmados de COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos confirmados')
    plot.tight_layout()
    plot.show()

def show_recovered_vs_countrys(dates_array, recovered_first_country, recovered_second_country, first_name, second_name):
    plot.plot(dates_array, recovered_first_country, linestyle='solid', color='blue', label=first_name)
    plot.plot(dates_array, recovered_second_country, linestyle='solid', color='green', label=second_name)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos recuperados de COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos recuperados')
    plot.tight_layout()
    plot.show()

def show_deaths_vs_countrys(dates_array, deaths_first_country, deaths_second_country, first_name, second_name):
    plot.plot(dates_array, deaths_first_country, linestyle='solid', color='blue', label=first_name)
    plot.plot(dates_array, deaths_second_country, linestyle='solid', color='green', label=second_name)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de decesos por COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de decesos')
    plot.tight_layout()
    plot.show()

def show_active_vs_countrys(dates_array, first_name, second_name):
    first_confirmed, first_recovered, first_deaths    = Tools.get_info_by_country_name(first_name)
    first_confirmed, first_recovered, first_deaths    = Tools.get_clear_vector_info(first_confirmed, first_recovered, first_deaths)
    second_confirmed, second_recovered, second_deaths = Tools.get_info_by_country_name(second_name)
    second_confirmed, second_recovered, second_deaths = Tools.get_clear_vector_info(second_confirmed, second_recovered, second_deaths)

    active_first_country  = get_active_cases(first_confirmed, first_recovered, first_deaths)
    active_second_country = get_active_cases(second_confirmed, second_recovered, second_deaths)

    plot.plot(dates_array, active_first_country, linestyle='solid', color='blue', label=first_name)
    plot.plot(dates_array, active_second_country, linestyle='solid', color='green', label=second_name)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos activos de COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos activos')
    plot.tight_layout()
    plot.show()

