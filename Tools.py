from datetime import date
import Validations
import csv
import re


# Rutas de los datasets
confirmed_cases_path = 'Raw data\\time_series_covid19_confirmed_global_iso3_regions.csv'
deaths_cases_path    = 'Raw data\\time_series_covid19_deaths_global_iso3_regions.csv'
recovered_cases_path = 'Raw data\\time_series_covid19_recovered_global_iso3_regions.csv'

# Variables globales
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
    # Devuleve 3 arreglos de enteros (casos confirmados, recuperados, decesos) con la información correspondoente
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
        # Sumando todoas las filas del arreglo
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

    for column_name in array_column_names:
        # Si el nombre de la columna coinside con la expresión regular
        if date_format_regex.match(column_name): 
            column_index.append( array_column_names.index(column_name) )
            

    first_index = column_index[0]
    last_index  = 1 + column_index[ len(column_index)-1 ]

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
    # Devulve una lista de todos los paises disponibles para consultar
    if Validations.file_exists([confirmed_cases_path]): # Si el archivo existe en la ruta
        with open(confirmed_cases_path, 'r') as confirmed_cases:
            reader        = csv.reader(confirmed_cases)
            country_names = []

            for vector in reader:
                country_names.append( vector[COUNTRY_COLUMN] )

            country_names.remove('Country/Region')
            country_names.remove('#country+name')
            country_names = list( dict.fromkeys(country_names) )

            for country in country_names:
                print(country)
    else:
        print('El archvo no existe en la ruta espesificada.')

def process_country_name(country_name):
    # --- EN DESAROLLO --- #
    # Devuelve el nombre procesado de un pais para encontrarlo en el dataset
    # country_name: Es el nomnre de un pais dado por el usuairo 
    print(country_name.split(' '))

def convert_to_date_type(dates_array):
    # Devuelve un arreglo de fechas de tipo date con el formato yyyy-mm-dd.
    # dates_array: es un arreglo de fechas de tipo string en formato mm/dd/yyyy
    date_type_array = []

    for dates in dates_array:
        dates        = dates.split('/')
        year         = '20' + dates[2]
        month        = dates[0]
        day          = dates[1]
        current_date = date( int(year), int(month), int(day) )
        date_type_array.append(current_date)

    return date_type_array

def indexes_to_remove_zeros(vector):
    # Devuleve las posiciones de inicio y final de la información de un vector
    # que no es igual a 0.
    # vector: Es un arreglo de enteros  
    first_index = -1
    last_index  = len(vector)

    for element in vector:
        if element == 0:
            first_index += 1

    return first_index, last_index

def get_confirmed_cases(country_name):
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
    column_names            = get_column_names()
    first_index, last_index = get_range_dates(column_names)
    dates_vector            = column_names[ first_index:last_index ]
    dates_vector            = convert_to_date_type(dates_vector)

    return dates_vector

def get_recovered_cases(country_name):
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

def get_active_cases(country_name):
    confirmed_cases, recovered_cases, deaths_cases = get_info_by_country_name(country_name)
    confirmed_cases                                = clear_vector(confirmed_cases)
    recovered_cases                                = clear_vector(recovered_cases)
    deaths_cases                                   = clear_vector(deaths_cases)

def nueve():
    print('nueve')

def diez():
    print('diez')

