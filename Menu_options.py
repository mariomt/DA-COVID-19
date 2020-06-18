import os
import sys
import tools.validations as Validations
import tools.data_visaulisation as plot
import tools.tools as Tools
from models.country import Country, NotFoundError
from tools.reader import Reader

reader = Reader()

# Variables globales
dates    = Tools.get_dates_vector(reader)
countrys = Country.show_all_names()
msg_vs_error = 'no se encuentran en la lista o no estan escritos correctamente.\n Revise nuestra lista países disponibles.'

# Input messages
MSG_INPUT_COUNTRY_NAME = 'Ingrese el nombre del país que desea consultar: '
MSG_INPUT_FIRST_COUNTRY_NAME = 'Ingrese el primer país: '
MSG_INPUT_SECOND_COUNTRY_NAME = 'Ingrese el segundo país: '

def show_info():
    # Imprime la información del sistema.
    print("""    
        Bienvenido. Aqui puedes consulatr información acerca del COVID-19, como casos confirmados, 
        recuperaciones, decesos y casos activos en el país que gustes consultar, o si lo prefieres, comparar 
        la información entre 2 países. Este programa se alimenta de la información proporcionada y recolectada 
        por the Johns Hopkins University Center for Systems Science and Engineering (JHU CCSE) de diversas 
        fuentes como the World Health Organization (WHO), DXY.cn, BNO News, National Health Commission of the 
        People’s Republic of China (NHC), China CDC (CCDC), Hong Kong Department of Health, Macau Government, 
        Taiwan CDC, US CDC, Government of Canada, Australia Government Department of Health, European Centre 
        for Disease Prevention and Control (ECDC), Ministry of Health Singapore (MOH), entre otros.

        Puedes consultar las fuentes en github: 
        https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports 
        o en el sitio web: https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases \n
        """)

def create_country(name):
    try:
        country = Country(name)
        return country
    except NotFoundError as ex:
        if str(ex)   == 'The country "{}" was not found.'.format(name):
            print(name + ' no se encuentra en la lista o no esta escrito correctamente.\nRevise nuestra lista países disponibles :(. \n')



def get_all_info_by_country():
    # Grafica y muestra toda la información de los casos recuperados, confirmados y decesos de un país.
    country_name = input(MSG_INPUT_COUNTRY_NAME)
    country = create_country(country_name)

    if country:
        raw_confirmed, raw_recovered, raw_deaths = country.get_data_info()
        confirmed_cases, recovered_cases, deaths_cases = Tools.get_clear_vector_info(raw_confirmed, raw_recovered, raw_deaths, reader)

        plot.show_all_country_info(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)
    else:
        wanna_do_something()

def get_confirmed_cases_by_country():
    # Grafica y muestra solo la información de los casos confirmados de un país.
    country_name = input(MSG_INPUT_COUNTRY_NAME)
    country = create_country(country_name)

    # Si el nombre del país no empiza con mayuscula o el campo esta vacio
    if country: 
        plot.show_country_confirmed_cases(dates, country)
    else:
        wanna_do_something()
        
def get_recovered_cases_by_country():
    # Grafica y muestra solo los casos recuperados de un país.
    country_name = input(MSG_INPUT_COUNTRY_NAME)
    country = create_country(country_name)

    if country: 
        plot.show_country_recovered_cases(dates, country)
    else:
        wanna_do_something()

def get_deaths_cases_by_country():
    # Grafica y muyestra solo los decesos de un país.
    country_name = input(MSG_INPUT_COUNTRY_NAME)
    country = create_country(country_name)

    # Si el nombre del país no empiza con mayuscula o el campo esta vacio
    if country:
        plot.show_country_deaths_cases(dates, country)
    else:
        print(country_name)
        wanna_do_something()

def get_active_cases_by_country():
    # Grafica y muestra solo los casos activos de un país.
    country_name = input(MSG_INPUT_COUNTRY_NAME)
    country = create_country(country_name)

    # Si el nombre del país no empiza con mayuscula o el campo esta vacio
    if country:
        confirmed_cases, recovered_cases, deaths_cases = country.get_data_info()

        confirmed_cases = Tools.clear_vector(confirmed_cases, reader)
        recovered_cases = Tools.clear_vector(recovered_cases, reader)
        deaths_cases    = Tools.clear_vector(deaths_cases, reader)

        plot.show_country_active_cases(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)
    else:
        wanna_do_something()

def get_vs_confirmed_cases():
    # Grafica y muestra una comparación entre ls casos conformados de 2 países.
    first_country  = input(MSG_INPUT_FIRST_COUNTRY_NAME)
    second_country = input(MSG_INPUT_SECOND_COUNTRY_NAME)

    country1 = create_country(first_country)
    country2 = create_country(second_country)

    if country1 and country2: 
        plot.show_confirmed_vs_countrys(dates, country1, country2)
    else:
        wanna_do_something()

def get_vs_recovered_cases():
    # Grafica y muestra una comparación entre los casos recuperados de 2 países.
    first_country  = input(MSG_INPUT_FIRST_COUNTRY_NAME)
    second_country = input(MSG_INPUT_SECOND_COUNTRY_NAME)

    country1 = create_country(first_country)
    country2 = create_country(second_country)

    if country1 and country2: 
        plot.show_recovered_vs_countrys(dates, country1, country2)
    else: 
        wanna_do_something()

def get_vs_deaths_cases():
    # Grafica y muestra una comparación de entre los decesos de 2 países.
    first_country  = input(MSG_INPUT_FIRST_COUNTRY_NAME)
    second_country = input(MSG_INPUT_SECOND_COUNTRY_NAME)

    country1 = create_country(first_country)
    country2 = create_country(second_country)

    if country1 and country2: 
        plot.show_deaths_vs_countrys(dates, country1, country2)
    else:
        wanna_do_something()
    
def get_vs_active_cases():
    # Grafica y muestra una comparación entre los casos a0ctivos entre 2 países.
    first_country  = input(MSG_INPUT_FIRST_COUNTRY_NAME)
    second_country = input(MSG_INPUT_SECOND_COUNTRY_NAME)

    country1 = create_country(first_country)
    country2 = create_country(second_country)

    if country1 and country2: 
        plot.show_active_vs_countrys(dates, country1, country2, reader)
    else:
        wanna_do_something()

def get_all_countrys(): 
    # Imprime una lista de todos los países disponibles en la base de datos.
    countrys = Country.show_all_names()

    print('# --- --- Lista de países --- --- #')
    for country in countrys:
        print(country)

def get_global_info():
    # Grafica y muestra la información.
    all_confirmed_cases, all_recovered_cases, all_deaths_cases = reader.global_info()
    plot.show_global_state(dates, all_confirmed_cases, all_recovered_cases, all_deaths_cases)

def exit():
    # Sale del programa
    print('bye')
    sys.exit()

def clear():
    # Limpia la terminal de comandos.
    clear = lambda: os.system('cls')

    return clear()

def get_global_death_rates():
    # Grafica los indices de mortalidad de cada país en una grafica de barras.
    death_rates = Tools.get_all_death_rates(Country.show_all_names(), Country, reader)
    plot.show_martality_bars(death_rates, reader)

def get_vs_general_by_country():
    # Grafica e imprime la información del estado general entre 2 países.
    first_country  = input(MSG_INPUT_FIRST_COUNTRY_NAME)
    second_country = input(MSG_INPUT_SECOND_COUNTRY_NAME)

    country1 = create_country(first_country)
    country2 = create_country(second_country)

    if country1 and country2: 
        plot.show_general_vs_country(dates, country1, country2, reader)
    else:
        wanna_do_something()

def get_daily_info_by_country():
    # Grafica e imprime la información de los casos confirmados diarios de un país.
    country_name = input(MSG_INPUT_COUNTRY_NAME)
    country = create_country(country_name)

    if country: 
        confirmed_vector = country.get_confirmed_cases()
        daily_cases      = Tools.get_daily_info(confirmed_vector)
        new_dates        = Tools.get_dates_vector(reader)

        plot.show_daily_confirmed_cases(new_dates, daily_cases, country)
    else:
        wanna_do_something()

def main_menu():
    # Opciones del menú principal.
    options_array = []

    def print_main_menu():
        # Imprime las opciones del menú principal.
        print("""# --- --- MENÚ PRINCIPAL --- --- #
    0 - Lista de todos los países disponibles
    1 - Estado de global de COVID-19
    2 - Estado de general de un país
    3 - Comparación de estado general entre 2 países
    4 - Casos confirmados de un país
    5 - Casos recuperados de un país
    6 - Decesos de un país
    7 - Casos activos de un país
    8 - Comparación de casos confirmados entre 2 países
    9 - Comparación de casos recuperados entre 2 países
    10 - Comparación de decesos entre 2 países
    11 - Comparacion de casos activos entre 2 países
    12 - Grafica de indices de mortalidad
    13 - Grafica de casos confirmados diarios de un país
    14 - Información del programa
    15 - Limpir la terminal
    16 - Salir""")

        option_selected = input('Seleccione una opción: ')
        return option_selected
        
    options = {
        # Diccionario de opciones del menú principal.
        '0': get_all_countrys,
        '1': get_global_info,
        '2': get_all_info_by_country,
        '3': get_vs_general_by_country,
        '4': get_confirmed_cases_by_country,
        '5': get_recovered_cases_by_country,
        '6': get_deaths_cases_by_country,
        '7': get_active_cases_by_country,
        '8': get_vs_confirmed_cases,
        '9': get_vs_recovered_cases,
        '10': get_vs_deaths_cases,
        '11': get_vs_active_cases,
        '12': get_global_death_rates,
        '13': get_daily_info_by_country,
        '14': show_info,
        '15': clear,
        '16': exit
    }   

    option_selected = print_main_menu()

    if option_selected == '0': # Mostrar los países
        options[option_selected]()
        main_menu()
    else:
        Validations.options_validator(options, option_selected)
        
    wanna_do_something()

def wanna_do_something():
    # Permite la continuidad del sistema hasta que el usuairo eliga salir.
    option_selected = input('¿Deseas realizar otra consulta? | 0 - No | 1 - Si |\n')

    if option_selected == '0':
        exit()
    elif option_selected == '1':
        main_menu()
    else:
        print('Opción invalida.')
        wanna_do_something()

