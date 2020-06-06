import sys
import Tools
import Validations
import Data_visaulisation as plot

dates = Tools.get_dates_vector()

def get_all_info_by_country():
    # Grafica y muestra toda la información de los casos recuperados, confirmados y decesos de un pais.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()

    raw_confirmed, raw_recovered, raw_deaths       = Tools.get_info_by_country_name(country_name)
    confirmed_cases, recovered_cases, deaths_cases = Tools.get_clear_vector_info(raw_confirmed, raw_recovered, raw_deaths)

    plot.show_all_country_info(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)

def get_confirmed_cases_by_country():
    # Grafica y muestra solo la información de los casos confirmados de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    confirmed_cases = Tools.get_confirmed_cases(country_name)

    plot.show_country_confirmed_cases(dates, confirmed_cases, country_name)

def get_recovered_cases_by_country():
    # Grafica y muestra solo los casos recuperados de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    recovered_cases = Tools.get_recovered_cases(country_name)
    plot.show_country_recovered_cases(dates, recovered_cases, country_name)
    
def get_deaths_cases_by_country():
    # Grafica y muyestra solo los decesos de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    deaths_cases = Tools.get_deaths_cases(country_name)
    plot.show_country_deaths_cases(dates, deaths_cases, country_name)

def get_active_cases_by_country():
    # Grafica y muestra solo los casos activos de un país.
    country_name = input('Ingrese el nombre del pais que desea consultar: ')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    confirmed_cases, recovered_cases, deaths_cases = Tools.get_info_by_country_name(country_name)
    confirmed_cases                                = Tools.clear_vector(confirmed_cases)
    recovered_cases                                = Tools.clear_vector(recovered_cases)
    deaths_cases                                   = Tools.clear_vector(deaths_cases)

    plot.show_country_active_cases(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)

def get_vs_confirmed_cases():
    # Grafica y muestra una comparación entre ls casos conformados de 2 paises.
    first_country = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    if Validations.capital_letter(first_country) and Validations.check_empty_country_name(first_country): 
        first_country = first_country.capitalize()

    if Validations.capital_letter(second_country) and Validations.check_empty_country_name(second_country): 
        second_country = second_country.capitalize()
    
    confirmed_first_country = Tools.get_confirmed_cases(first_country)
    confirmed_second_country = Tools.get_confirmed_cases(second_country)

    plot.show_confirmed_vs_countrys(dates, confirmed_first_country, confirmed_second_country, first_country, second_country)

def get_vs_recovered_cases():
    # Grafica y muestra una comparación entre los casos recuperados de 2 paises.
    first_country = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    if Validations.capital_letter(first_country) and Validations.check_empty_country_name(first_country): 
        first_country = first_country.capitalize()

    if Validations.capital_letter(second_country) and Validations.check_empty_country_name(second_country): 
        second_country = second_country.capitalize()

    recovered_first_country  = Tools.get_recovered_cases(first_country)
    recovered_second_country = Tools.get_recovered_cases(second_country)

    plot.show_recovered_vs_countrys(dates, recovered_first_country, recovered_second_country, first_country, second_country)

def get_vs_deaths_cases():
    # Grafica y muestra una comparación de entre los decesos de 2 paises.
    first_country = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    if Validations.capital_letter(first_country) and Validations.check_empty_country_name(first_country): 
        first_country = first_country.capitalize()

    if Validations.capital_letter(second_country) and Validations.check_empty_country_name(second_country): 
        second_country = second_country.capitalize()

    deaths_first_country   = Tools.get_deaths_cases(first_country)
    deaths_seacond_country = Tools.get_deaths_cases(second_country)

    plot.show_deaths_vs_countrys(dates, deaths_first_country, deaths_seacond_country, first_country, second_country)

def get_vs_active_cases():
    # Grafica y muestra una comparación entre los casos a0ctivos entre 2 paises.
    first_country = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    if Validations.capital_letter(first_country) and Validations.check_empty_country_name(first_country): 
        first_country = first_country.capitalize()

    if Validations.capital_letter(second_country) and Validations.check_empty_country_name(second_country): 
        second_country = second_country.capitalize()

    plot.show_active_vs_countrys(dates, first_country, second_country)

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
    print('bye')
    sys.exit()

def get_global_death_rates():
    # Grafica los indices de mortalidad de cada país en una grafica de barras.
    death_rates = Tools.get_all_death_rates()
    plot.show_martality_bars(death_rates)

def get_vs_general_by_country():
    # Grafica e imprime la información del estado general entre 2 paises.
    first_country = input('Ingrese el primer país: ')
    second_country = input('Ingrese el segundo país: ')

    if Validations.capital_letter(first_country) and Validations.check_empty_country_name(first_country): 
        first_country = first_country.capitalize()

    if Validations.capital_letter(second_country) and Validations.check_empty_country_name(second_country): 
        second_country = second_country.capitalize()

    plot.show_general_vs_country(dates, first_country, second_country)

    # wanna_do_something()

def main_menu():
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
    13 - Salir""")

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
        '13': exit
    }   

    option_selected = print_main_menu()

    if option_selected == '0':
        options[option_selected]()
        main_menu()
    else:
        Validations.options_validator(options, option_selected)
        
    wanna_do_something()

def wanna_do_something():
    option_selected = input('¿Deseas realizar otra consulta? | 0 - No | 1 - Si |\n')

    if option_selected == '0':
        exit()
    elif option_selected == '1':
        main_menu()
    else:
        print('Opción invalida.')
        wanna_do_something()