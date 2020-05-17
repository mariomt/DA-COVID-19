from datetime import date
import numpy as np
import Validations
import csv
import re


# Rutas de los datasets
confirmed_cases_path = 'Raw data\\time_series_covid19_confirmed_global_iso3_regions.csv'
deaths_cases_path = 'Raw data\\time_series_covid19_deaths_global_iso3_regions.csv'
recovered_cases_path = 'Raw data\\time_series_covid19_recovered_global_iso3_regions.csv'

# Variables globales
COUNTRY_COLUMN = 1

def get_info_by_country_name(country):
    # Devuelve un arreglo con toda la información de un pais
    # country: Es el nombre de un pais dado por el usuario.
    if Validations.file_exists(confirmed_cases_path) and Validations.check_empty_country_name(country):
        with open(confirmed_cases_path, 'r') as confirmed_cases:
            reader = csv.reader(confirmed_cases)
            country_raw_info = []

            for row in reader:
                if row[COUNTRY_COLUMN] == country:
                    country_raw_info.append(row)
            
            return country_raw_info
    else:
        print('El archvo no existe en la ruta espesificada.')

def get_column_names():
    # Obtiene el primer renglon del dataset
    if Validations.file_exists(confirmed_cases_path): # Si el archivo existe
        with open(confirmed_cases_path, 'r') as confirmed_cases:
            reader = csv.reader(confirmed_cases)

            return next(reader)
    else:
        print('El archvo no existe en la ruta espesificada.')

def get_clear_vector_info(country_raw_info):
    # Devuleve un arreglo solo con la información correspondoente a las
    # a fechas de un pais antes seleccionado.
    # country_raw_info: Es un arreglo con toda la información de un pais.
    column_names = get_column_names()
    fisrt_index, last_index = get_range_dates(column_names)
    dates_cases = []
    dates = []
    
    for vector in country_raw_info:
        dates_cases.append(vector[ fisrt_index:last_index ])

    dates_cases = convert_to_int(dates_cases)

    if len(country_raw_info) > 1: # Si el arreglo tiene mas de una fila
        dates_cases = add_matrix_to_vector(dates_cases)

    dates = convert_to_date_type( column_names[fisrt_index:last_index] ) 
    return dates_cases, dates

def get_range_dates(array_column_names):
    # Verifica si el nombre de la columna es una fecha.
    # array_column_names: Es un arreglo con los nombres de las clumnas 
    # (el primer renglon).
    date_format_regex = re.compile(r'(\d{1,2}\/\d{1,2}\/\d{2})')
    column_index = []

    for column_name in array_column_names:
        # Si el nombre de la columna coinside con la expresión regular
        if date_format_regex.match(column_name): 
            column_index.append( array_column_names.index(column_name) )
    
    first_index = column_index[0]
    last_index = column_index[ len(column_index)-1 ]

    return first_index, last_index

def convert_to_int(dates_cases):
    # Tranforma una matriz de numeros de tipo string en una matriz de integers.
    # dates_cases: es un matriz de con numeros de tipo string.
    int_dates_cases = [ [int(element) for element in vector] for vector in dates_cases ]
    return int_dates_cases

def add_matrix_to_vector(int_dates_cases):
    # Suma todos los valores de una matriz y devuelve un vector con la suma.
    # int_dates_cases: Es una matriz de enteros con los casos por fecha.
    summed_vector = [ sum(element) for element in zip(*int_dates_cases) ]
    return summed_vector

def show_all_countrys():
    # Devulve una lista de todos los paises disponibles para consultar
    if Validations.file_exists(confirmed_cases_path): # Si el archivo existe en la ruta
        with open(confirmed_cases_path, 'r') as confirmed_cases:
            reader = csv.reader(confirmed_cases)
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
    print(country_name.split(' '))

def convert_to_date_type(dates_array):
    date_type_array = []

    for dates in dates_array:
        dates = dates.split('/')
        year = '20' + dates[2]
        month = dates[0]
        day = dates[1]
        current_date = date( int(year), int(month), int(day) )
        date_type_array.append(current_date)

    return date_type_array

