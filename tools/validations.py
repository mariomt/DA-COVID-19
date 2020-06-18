import re

# --- Validaciones ---- #

def options_validator(options, option_selected):
    # Verifica que una opción dada por el usuairo exista en la lista de opciones disponibles.
    # options: Es un diccionario con las opciones y sus funciones.
    # option_selected: Es la opción seleccioanda por el usuario.
    for option in options:
        if option_selected == option:
            return options[option_selected]()
    
    print(option_selected + ' no es una opción disponible en nuestro menú. :(')
    option_selected = input('Revise nuestro menú e intentelo nuevamente: ')

    options_validator(options, option_selected)

def country_validator(country_name, countrys):
    # Verifica que exista un país dado por el usuairo en la lista de países disponibles.
    # country_name: Es el nombre del país dado por el usuario.
    # countrys: Es la lista de países disponibles. 
    country_name   = country_name.lower().strip()
    lower_countrys = countrys_to_lower(countrys)
    flag           = False 
    msg_error      = country_name + ' no se encuentra en la lista o no esta escrito correctamente.\n Revise nuestra lista países disponibles. \n' 

    if country_name in lower_countrys:
        position = lower_countrys.index(country_name)
        flag = True
        
        return countrys[position], flag
    else:
        return msg_error, flag


def countrys_to_lower(countrys):
    # Devuleve un arreglo de strings en minusculas.
    # countrys: Es un arreglo de strings.
    lower_countrys = []

    for country in countrys:
        lower_countrys.append(country.lower())

    return lower_countrys

