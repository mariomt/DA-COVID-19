import re

# --- Validaciones ---- #
def capital_letter(country_name):
    if not re.search('^[A-Z]', country_name): # Si el nombre del pais no empiza con mayuscula
        return True
    else:
        return False

def file_exists(files_path):
    # Verifica que exista el archivo en la ruta proporsionada.
    # files_path: Es un arreglo de string que contiene rutas de archivos.
    for file in files_path:
        try:
            open(file, 'r')
            return True
        except IOError:
            return False

def check_empty_country_name(country_space):
    # Verifica que el nombre del paise proporsionado por el usuario no 
    # este en blanco.
    # country: Es el nombre del pais porporsionado por el usuario.
    if not country_space or not country_space.strip():
        return False
        print('El campo del pais esta en blanco o no es valido')
    else:
        return True

def options_validator(options, option_selected):
    for option in options:
        if option_selected == option:
            return options[option_selected]()
    
    print(option_selected + ' no es una opción disponible en nuestro menu. :(')
    option_selected = input('Revise nuestro menu e intentelo nuevamente: ')

    options_validator(options, option_selected)
    

def country_validator(country_name, countrys):
    country_name = country_name.lower().strip()

    for country in countrys:
        country = country.lower().strip()

        if country_name in country:
            print(':) HERE!')
            break
        else:
            print(':(')

