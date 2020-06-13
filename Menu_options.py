import os
import sys
import Tools
import Validations
import data_visaulisation as plot

# Variables globales
dates    = Tools.get_dates_vector()
countrys = Tools.show_all_countrys()
msg_vs_error = 'no se encuentran en la lista o no estan escritos correctamente.\n Revise nuestra lista paises disponibles.'

def show_info():
    # Imprime la información del sistema.
    print("""    Bienvenido. Aqui puedes consulatr información acerca del COVID-19, como casos confirmados, 
        recuperaciones, decesos y casos activos en el país que gustes consultar, o si lo prefieres, comparar 
        la información entre 2 paises. Este programa se alimenta de la información proporsionada y recolectada 
        por the Johns Hopkins University Center for Systems Science and Engineering (JHU CCSE) de diversas 
        fuentes como the World Health Organization (WHO), DXY.cn, BNO News, National Health Commission of the 
        People’s Republic of China (NHC), China CDC (CCDC), Hong Kong Department of Health, Macau Government, 
        Taiwan CDC, US CDC, Government of Canada, Australia Government Department of Health, European Centre 
        for Disease Prevention and Control (ECDC), Ministry of Health Singapore (MOH), entre otros.

        Puedes consultar las fuentes en github: 
        https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports 
        o en el sitio web: https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases \n""")

def get_all_info_by_country():
    # Grafica y muestra toda la información de los casos recuperados, confirmados y decesos de un pais.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    country_name, flag = Validations.country_validator(country_name, countrys)

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if flag: 
        raw_confirmed, raw_recovered, raw_deaths       = Tools.get_info_by_country_name(country_name)
        confirmed_cases, recovered_cases, deaths_cases = Tools.get_clear_vector_info(raw_confirmed, raw_recovered, raw_deaths)

        plot.show_all_country_info(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)
    else:
        print(country_name)
        wanna_do_something()

def get_confirmed_cases_by_country():
    # Grafica y muestra solo la información de los casos confirmados de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    country_name, flag = Validations.country_validator(country_name, countrys)

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if flag: 
        confirmed_cases = Tools.get_confirmed_cases(country_name)

        plot.show_country_confirmed_cases(dates, confirmed_cases, country_name)
    else:
        print(country_name)
        wanna_do_something()
        
def get_recovered_cases_by_country():
    # Grafica y muestra solo los casos recuperados de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    country_name, flag = Validations.country_validator(country_name, countrys)

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if flag: 
        recovered_cases = Tools.get_recovered_cases(country_name)
        plot.show_country_recovered_cases(dates, recovered_cases, country_name)
    else:
        print(country_name)
        wanna_do_something()

def get_deaths_cases_by_country():
    # Grafica y muyestra solo los decesos de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    country_name, flag = Validations.country_validator(country_name, countrys)

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if flag:    
        deaths_cases = Tools.get_deaths_cases(country_name)
        plot.show_country_deaths_cases(dates, deaths_cases, country_name)
    else:
        print(country_name)
        wanna_do_something()

def get_active_cases_by_country():
    # Grafica y muestra solo los casos activos de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    country_name, flag = Validations.country_validator(country_name, countrys)

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if flag:
        confirmed_cases, recovered_cases, deaths_cases = Tools.get_info_by_country_name(country_name)

        confirmed_cases = Tools.clear_vector(confirmed_cases)
        recovered_cases = Tools.clear_vector(recovered_cases)
        deaths_cases    = Tools.clear_vector(deaths_cases)

        plot.show_country_active_cases(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)
    else:
        print(country_name)
        wanna_do_something()

def get_vs_confirmed_cases():
    # Grafica y muestra una comparación entre ls casos conformados de 2 paises.
    first_country  = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    first_country, flag_1   = Validations.country_validator(first_country, countrys)
    second_country, flag_2 = Validations.country_validator(second_country, countrys)

    if flag_1 and flag_2: 
        confirmed_first_country  = Tools.get_confirmed_cases(first_country)
        confirmed_second_country = Tools.get_confirmed_cases(second_country)

        plot.show_confirmed_vs_countrys(dates, confirmed_first_country, confirmed_second_country, first_country, second_country)
    else:
        print(first_country + ' o ' + second_country + ' ' + msg_vs_error)
        wanna_do_something()

def get_vs_recovered_cases():
    # Grafica y muestra una comparación entre los casos recuperados de 2 paises.
    first_country  = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    first_country, flag_1  = Validations.country_validator(first_country, countrys)
    second_country, flag_2 = Validations.country_validator(second_country, countrys)

    if flag_1 and flag_2: 
        recovered_first_country  = Tools.get_recovered_cases(first_country)
        recovered_second_country = Tools.get_recovered_cases(second_country)

        plot.show_recovered_vs_countrys(dates, recovered_first_country, recovered_second_country, first_country, second_country)
    else: 
        print(first_country + ' o ' + second_country + ' ' + msg_vs_error)
        wanna_do_something()

def get_vs_deaths_cases():
    # Grafica y muestra una comparación de entre los decesos de 2 paises.
    first_country  = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    first_country, flag_1  = Validations.country_validator(first_country, countrys)
    second_country, flag_2 = Validations.country_validator(second_country, countrys)

    if flag_1 and flag_2: 
        deaths_first_country   = Tools.get_deaths_cases(first_country)
        deaths_seacond_country = Tools.get_deaths_cases(second_country)

        plot.show_deaths_vs_countrys(dates, deaths_first_country, deaths_seacond_country, first_country, second_country)
    else:
        print(first_country + ' o ' + second_country + ' ' + msg_vs_error)
        wanna_do_something()
    
def get_vs_active_cases():
    # Grafica y muestra una comparación entre los casos a0ctivos entre 2 paises.
    first_country  = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    first_country, flag_1  = Validations.country_validator(first_country, countrys)
    second_country, flag_2 = Validations.country_validator(second_country, countrys) 

    if flag_1 and flag_2: 
        plot.show_active_vs_countrys(dates, first_country, second_country)
    else:
        print(first_country + ' o ' + second_country + ' ' + msg_vs_error)
        wanna_do_something()

def get_all_countrys(): 
    # Imprime una lista de todos los paises disponibles en la base de datos.
    countrys = Tools.show_all_countrys()

    print('# --- --- Lista de paises --- --- #')
    for country in countrys:
        print(country)

def get_global_info():
    # Grafica y muestra la información.
    all_confirmed_cases, all_recovered_cases, all_deaths_cases = Tools.global_info()
    plot.show_global_state(dates, all_confirmed_cases, all_recovered_cases, all_deaths_cases)

def exit():
    # Sale del programa
    clear()
    print('bye')
    sys.exit()

def clear():
    # Limpia la terminal de comandos.
    clear = lambda: os.system('cls')

    return clear()

def get_global_death_rates():
    # Grafica los indices de mortalidad de cada país en una grafica de barras.
    death_rates = Tools.get_all_death_rates()
    plot.show_martality_bars(death_rates)

def get_vs_general_by_country():
    # Grafica e imprime la información del estado general entre 2 paises.
    first_country  = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    first_country, flag_1  = Validations.country_validator(first_country, countrys)
    second_country, flag_2 = Validations.country_validator(second_country, countrys)

    if flag_1 and flag_2: 
        plot.show_general_vs_country(dates, first_country, second_country)
    else:
        print(first_country + ' o ' + second_country + ' ' + msg_vs_error)
        wanna_do_something()

def get_daily_info_by_country():
    # Grafica e imprime la información de los casos confirmados diarios de un país.
    country_name = input('Ingrese el nombre del país que desea consultar: ')
    
    country_name, flag = Validations.country_validator(country_name, countrys)

    if flag: 
        confirmed_vector = Tools.get_confirmed_cases(country_name)
        daily_cases      = Tools.get_daily_info(confirmed_vector)
        new_dates        = Tools.get_dates_vector()

        plot.show_daily_confirmed_cases(new_dates, daily_cases, country_name)
    else:
        print(country_name)
        wanna_do_something()

def main_menu():
    # Opciones del menu principal.
    options_array = []

    def print_main_menu():
        # Imprime las opciones del menu principal.
        print("""# --- --- MENU PRINCIPAL --- --- #
    0 - Lista de todos los paises disponibles
    1 - Estado de global de COVID-19
    2 - Estado de general de un país
    3 - Comparación de estado general entre 2 paises
    4 - Casos confirmados de un país
    5 - Casos recuperados de un pais
    6 - Decesos de un pais
    7 - Casos activos de un pais
    8 - Comparación de casos confirmados entre 2 paises
    9 - Comparación de casos recuperados entre 2 paises
    10 - Comparación de decesos entre 2 paises
    11 - Comparacion de casos activos entre 2 paises
    12 - Grafica de indices de mortalidad
    13 - Grafica de casos confirmados diarios de un país
    14 - Información del programa
    15 - Limpir la terminal
    16 - Salir""")

        option_selected = input('Seleccione una opción: ')
        return option_selected
        
    options = {
        # Diccionario de opciones del menu principal.
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

    if option_selected == '0': # Mostrar los paises
        options[option_selected]()
        main_menu()
    elif option_selected == '14': # Mostrar información del sistema
        clear()
        options[option_selected]()
    else:
        Validations.options_validator(options, option_selected)
        
    wanna_do_something()

def wanna_do_something():
    # Permite la continuidad del sistema hasta que el usuairo eliga salir.
    option_selected = input('¿Deseas realizar otra consulta? | 0 - No | 1 - Si |\n')

    if option_selected == '0':
        exit()
    elif option_selected == '1':
        clear()
        main_menu()
    else:
        clear()
        print('Opción invalida.')
        wanna_do_something()

