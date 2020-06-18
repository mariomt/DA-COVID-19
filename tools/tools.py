from datetime import date
import csv
import re
import config


def get_clear_vector_info(raw_confirmed, raw_recovered, raw_deaths, reader):
    # Devuleve 3 arreglos de enteros (casos confirmados, recuperados y decesos) con la información correspondoente
    # a las fechas de un pais antes seleccionado.
    # raw_confirmed: Es un arreglo de strings con toda la información los casos confirmados.
    # raw_recovered:  Es un arreglo de strings con toda la información los casos recuperados.
    # raw_deaths: Es un arreglo de strings con toda la información los decesos.
    column_names            = reader.get_first_row(config.CONFIRMED_CASES_PATH)
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

def clear_vector(raw_array, reader):
    # Devuleve un arreglo de enteros con la información correspondiente a las fechas.
    # raw_array: Es un arreglo de string con toda la información de un pais.
    column_names            = reader.get_first_row(config.CONFIRMED_CASES_PATH)
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


def convert_to_date_type(dates_array):
    # Devuelve un arreglo de fechas de tipo date con el formato yyyy-mm-dd.
    # dates_array: es un arreglo de fechas de tipo string en formato mm/dd/yyyy.
    date_type_array = []

    for dates in dates_array:
        dates = dates.split('/')
        year = '20' + dates[2]
        month = dates[0]
        day = dates[1]
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

def get_first_case_index(vector):
    # Devuleve la posición de un arreglo en la que deja de ser cero.
    # vector: Es un arreglo de enteros. 
    index = 0

    for n in vector:
        if n == 0:
            index += 1
        else:
            break

    return index




def get_dates_vector(reader):
    # Devuelve un arreglo de fechas en formato date correpondiente a todas las fechas comprendidas en el dataset.
    column_names            = reader.get_first_row(config.CONFIRMED_CASES_PATH)
    first_index, last_index = get_range_dates(column_names)
    dates_vector            = column_names[ first_index:last_index ]
    dates_vector            = convert_to_date_type(dates_vector)

    return dates_vector



def get_country_death_rate(country, reader):
    # Devuleve el indice porcentual de mortalidad de un país dado.
    # country_name: Es el nombre del país. 
    confirmed = country.get_confirmed_cases()
    deaths    = country.get_deaths_cases()
    
    last_info_column = len(confirmed)-1

    confirmed = confirmed[last_info_column]
    deaths    = deaths[last_info_column]

    death_rate = (deaths / confirmed)*100
    death_rate = round(death_rate, 2)

    return death_rate

def get_all_death_rates(countries, Country ,reader):
    # Devuleve un diccionario (o un arreglo en formato nombre:valor) con los idnices porcentuales
    # de mortalidad de todos los países. 
    death_rates = {}

    for country in countries:
        objCountry = Country(country)
        death_rates[country] = get_country_death_rate(objCountry, reader)
    
    return death_rates

def get_daily_info(vector):
    # Devuelve un arreglo de enteros con la información de casos diarios de un arreglo dado.
    # vector: Es un arreglo de enteros
    daily_info = []
    size = len(vector)

    for n in range(size):
        if not n+1 == size-1:
            daily_info.append( vector[n+1] - vector[n] )
        else: 
            break

    return daily_info

def get_average(vector):
    # Devuelve el promedio de un vector de enteros.
    # vector: Es un arreglo de enteros
    cases = sum(vector)
    days = len(vector)
    average = round(cases / days, 2)

    return average