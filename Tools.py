from datetime import date
import Validations
import csv
import re

# Variables globales
# Rutas de los datasets
confirmed_cases_path = 'Raw data\\time_series_covid19_confirmed_global_iso3_regions.csv'
deaths_cases_path    = 'Raw data\\time_series_covid19_deaths_global_iso3_regions.csv'
recovered_cases_path = 'Raw data\\time_series_covid19_recovered_global_iso3_regions.csv'

COUNTRY_COLUMN = 1
FILES_PATH     = [confirmed_cases_path, deaths_cases_path, recovered_cases_path]

def get_info_by_country_name(country):
    # Devuelve 3 arreglos (casos confirmados, recuperados y decesos) de tipo string con la 
    # información completa de un pais dado.
    # country: Es el nombre de un pais dado por el usuario (string).
    raw_confirmed_cases = []
    raw_recovered_cases = [] 
    raw_deaths_cases    = []

    if Validations.file_exists(FILES_PATH):
        with open(confirmed_cases_path, 'r') as confirmed_cases: # extrayendo información de casos confirmados
            reader             = csv.reader(confirmed_cases)
            confirmed_raw_info = []

            for row in reader:
                if row[COUNTRY_COLUMN] == country:
                    confirmed_raw_info.append(row)
            
            raw_confirmed_cases = confirmed_raw_info

        with open(recovered_cases_path, 'r') as recovered_cases: # extrayendo información de casos de recuperados
            reader             = csv.reader(recovered_cases)
            recovered_raw_info = []

            for row in reader:
                if row[COUNTRY_COLUMN] == country:
                    recovered_raw_info.append(row)

            raw_recovered_cases = recovered_raw_info

        with open(deaths_cases_path, 'r') as deaths_cases: # extrayendo información de casos decesos
            reader          = csv.reader(deaths_cases)
            deaths_raw_info = []

            for row in reader:
                if row[COUNTRY_COLUMN] == country:
                    deaths_raw_info.append(row)

            raw_deaths_cases = deaths_raw_info

        return raw_confirmed_cases, raw_recovered_cases, raw_deaths_cases

    else:
        print('La ruta de uno de los archivos no existe o es incorrecta.')

def get_column_names():
    # Obtiene el primer renglon del dataset
    if Validations.file_exists([confirmed_cases_path]): # Si el archivo existe
        with open(confirmed_cases_path, 'r') as confirmed_cases:
            reader = csv.reader(confirmed_cases)
            return next(reader)
    else:
        print('El archvo no existe en la ruta espesificada.')

def get_clear_vector_info(raw_confirmed, raw_recovered, raw_deaths):
    # Devuleve 3 arreglos de enteros (casos confirmados, recuperados y decesos) con la información correspondoente
    # a las fechas de un pais antes seleccionado.
    # raw_confirmed: Es un arreglo de strings con toda la información los casos confirmados.
    # raw_recovered:  Es un arreglo de strings con toda la información los casos recuperados.
    # raw_deaths: Es un arreglo de strings con toda la información los decesos.
    column_names            = get_column_names()
    fisrt_index, last_index = get_range_dates(column_names)
    confirmed_cases         = []
    recovered_cases         = []
    deaths_cases            = []

    # Aislando las columnas correspondientes a las fechas
    for vector in raw_confirmed:
        confirmed_cases.append(vector[ fisrt_index:last_index ])

    for vector in raw_recovered:
        recovered_cases.append(vector[ fisrt_index:last_index ])

    for vector in raw_deaths:
        deaths_cases.append(vector[ fisrt_index:last_index ])

    # Convirtiendo los arreglos de tipo string a int
    confirmed_cases = convert_to_int(confirmed_cases)
    recovered_cases = convert_to_int(recovered_cases)
    deaths_cases    = convert_to_int(deaths_cases)

    if len(raw_confirmed) > 1: # Si el arreglo tiene mas de una fila
        # Sumando todas las filas del arreglo
        confirmed_cases = add_matrix_to_vector(confirmed_cases)
        recovered_cases = add_matrix_to_vector(recovered_cases)
        deaths_cases    = add_matrix_to_vector(deaths_cases)

    if len(confirmed_cases) == 1: 
        # Por procedimiento de otros metodos hay ocaciones en las que los arreglos de enteros
        # estan en un lista de arreglos o lista de listas. Aqui se valida si hay una lista 
        # dentro de otra, de ser asi se iguala a la lista que se encuentra dentro. 
        confirmed_cases = confirmed_cases[0]
        recovered_cases = recovered_cases[0]
        deaths_cases    = deaths_cases[0]

    return confirmed_cases, recovered_cases, deaths_cases

def get_range_dates(array_column_names):
    # Verifica si el nombre de la columna es una fecha.
    # array_column_names: Es un arreglo con los nombres de las clumnas 
    # (el primer renglon).
    date_format_regex = re.compile(r'(\d{1,2}\/\d{1,2}\/\d{2,4})')
    column_index      = []
    last_index        = 1

    for column_name in array_column_names:
        # Si el nombre de la columna coinside con la expresión regular de una fecha
        if date_format_regex.match(column_name): 
            column_index.append( array_column_names.index(column_name) )
            
    first_index = column_index[0]
    last_index  += column_index[ len(column_index)-1 ]

    return first_index, last_index

def convert_to_int(dates_cases):
    # Tranforma una matriz de numeros de tipo string en una matriz de integers.
    # dates_cases: es un vector de con numeros de tipo string.
    int_dates_cases = [ [int(element) for element in vector] for vector in dates_cases ]
    return int_dates_cases

def add_matrix_to_vector(int_dates_cases):
    # Suma todos los valores de una matriz y devuelve un vector con la suma.
    # int_dates_cases: Es una matriz de enteros con los casos por fecha.
    summed_vector = [ sum(element) for element in zip(*int_dates_cases) ]
    return summed_vector

def show_all_countrys():
    # Devulve una lista de todos los paises disponibles para consultar.
    if Validations.file_exists([confirmed_cases_path]): # Si el archivo existe en la ruta
        with open(confirmed_cases_path, 'r') as confirmed_cases:
            reader        = csv.reader(confirmed_cases)
            country_names = []

            for vector in reader:
                country_names.append( vector[COUNTRY_COLUMN] )

            country_names.remove('Country/Region')
            country_names.remove('#country+name')
            country_names = list( dict.fromkeys(country_names) )

            return country_names
    else:
        print('El archvo no existe en la ruta espesificada.')

def convert_to_date_type(dates_array):
    # Devuelve un arreglo de fechas de tipo date con el formato yyyy-mm-dd.
    # dates_array: es un arreglo de fechas de tipo string en formato mm/dd/yyyy.
    date_type_array = []

    for dates in dates_array:
        dates        = dates.split('/')
        year         = '20' + dates[2]
        month        = dates[0]
        day          = dates[1]
        current_date = date( int(year), int(month), int(day) )
        date_type_array.append(current_date)

    return date_type_array

def remove_zeros(vector):
    # Devuleve un arreglo de enteros que no contengan ceros.
    # vector: Es un arreglo de enteros.
    new_vector = []

    for n in vector:
        if not n == 0:
            new_vector.append(n)

    return new_vector

def get_first_case_index(vector_confirmed):
    index = 0

    for n in vector_confirmed:
        if n == 0:
            index += 1

    return index

def get_confirmed_cases(country_name):
    # Devuleve un arreglo de enteros que contiene la información sobre los casos confirmados de un país.
    # country_name: Es el nombre del pais.
    confirmed_cases = []

    if Validations.file_exists([confirmed_cases_path]):
        with open(confirmed_cases_path, 'r') as raw_confirmed_cases:
            reader = csv.reader(raw_confirmed_cases)

            for row in reader:
                if row[COUNTRY_COLUMN] == country_name:
                    confirmed_cases.append(row)
    else:
        print('El archvo no existe en la ruta espesificada.')

    confirmed_cases = clear_vector(confirmed_cases)
    return confirmed_cases

def clear_vector(raw_array):
    # Devuleve un arreglo de enteros con la información correspondiente a las fechas.
    # raw_array: Es un arreglo de string con toda la información de un pais.
    column_names            = get_column_names()
    first_index, last_index = get_range_dates(column_names)
    clear_vector            = []

    for vector in raw_array:
        clear_vector.append(vector[ first_index:last_index ])

    clear_vector = convert_to_int(clear_vector)

    if len(raw_array) > 1:
        clear_vector = add_matrix_to_vector(clear_vector)

    if len(clear_vector) == 1:
        clear_vector = clear_vector[0]

    return clear_vector

def get_dates_vector():
    # Devuelve un arreglo de fechas en formato date correpondiente a todas las fechas comprendidas en el dataset.
    column_names            = get_column_names()
    first_index, last_index = get_range_dates(column_names)
    dates_vector            = column_names[ first_index:last_index ]
    dates_vector            = convert_to_date_type(dates_vector)

    return dates_vector

def get_recovered_cases(country_name):
    # Devuelve un arreglo de enteros con la información de los casos recuperados de un país.
    # country_name: Es el nomnre del país.
    recovered_cases = []

    if Validations.file_exists([recovered_cases_path]):
        with open(recovered_cases_path, 'r') as raw_recovered_cases:
            reader = csv.reader(raw_recovered_cases)

            for row in reader:
                if row[COUNTRY_COLUMN] == country_name:
                    recovered_cases.append(row)
    else:
        print('El archvo no existe en la ruta espesificada.')

    recovered_cases = clear_vector(recovered_cases)
    return recovered_cases

def get_deaths_cases(country_name):
    # Devuelve un arreglo de enteros con la información de los decesos de un país.
    # country_name: Es el nombre del país.
    deaths_cases = []

    if Validations.file_exists([deaths_cases_path]):
        with open(deaths_cases_path, 'r') as raw_deaths_cases:
            reader = csv.reader(raw_deaths_cases)

            for row in reader:
                if row[COUNTRY_COLUMN] == country_name:
                    deaths_cases.append(row)
    else:
        print('El archvo no existe en la ruta espesificada.')

    deaths_cases = clear_vector(deaths_cases)
    return deaths_cases

def global_info():
    # Devuleve 3 arreglos (casos confirmados, recuperados y decesos) de enteros con la información de todos los paises del dataset.
    all_confirmed_cases = []
    all_recovered_cases = []
    all_deaths_cases    = []

    if Validations.file_exists(FILES_PATH):
        with open(confirmed_cases_path, 'r') as raw_confirmed_cases:
            reader = csv.reader(raw_confirmed_cases)

            for row in reader:
                if not row[COUNTRY_COLUMN] == 'Country/Region' and not row[COUNTRY_COLUMN] == '#country+name':
                    all_confirmed_cases.append(row)

        with open(recovered_cases_path, 'r') as raw_recovered_cases:
            reader = csv.reader(raw_recovered_cases)

            for row in reader:
                if not row[COUNTRY_COLUMN] == 'Country/Region' and not row[COUNTRY_COLUMN] == '#country+name':
                    all_recovered_cases.append(row)

        with open(deaths_cases_path, 'r') as raw_deaths_cases:
            reader = csv.reader(raw_deaths_cases)

            for row in reader:
                if not row[COUNTRY_COLUMN] == 'Country/Region' and not row[COUNTRY_COLUMN] == '#country+name':
                    all_deaths_cases.append(row)
    else:
        print('El archvo no existe en la ruta espesificada.')

    all_confirmed_cases, all_recovered_cases, all_deaths_cases = get_clear_vector_info(all_confirmed_cases, all_recovered_cases, all_deaths_cases)
    
    return all_confirmed_cases, all_recovered_cases, all_deaths_cases

def main_menu():
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

def get_country_death_rate(country_name):
    # Devuleve el indice porcentual de mortalidad de un país dado.
    # country_name: Es el nombre del país. 
    confirmed = get_confirmed_cases(country_name)
    deaths    = get_deaths_cases(country_name)
    
    last_info_column = len(confirmed)-1

    confirmed = confirmed[last_info_column]
    deaths    = deaths[last_info_column]

    death_rate = (deaths / confirmed)*100
    death_rate = round(death_rate, 2)

    return death_rate

def get_all_death_rates():
    # Devuleve un diccionario (o un arreglo en formato nombre:valor) con los idnices porcentuales
    # de mortalidad de todos los paises. 
    death_rates = {}
    countrys    = show_all_countrys()

    for country in countrys:
        death_rates[country] = get_country_death_rate(country)
    
    return death_rates