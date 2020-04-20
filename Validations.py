import re

# --- Validaciones ---- #

def capital_letter(country_name):
    if not re.search('^[A-Z]', country_name): # Si el nombre del pais no empiza con mayuscula
        return True
    else:
        return False

def file_exists(file_path):
    # Verifica que exista el archivo en la ruta proporsionada.
    # file_path: Es un string que contiene la ruta del dataset.
    try:
        open(file_path, 'r')
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