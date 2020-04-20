import Tools
import Validations

country_name = input('Ingrese el nombre del pais que desea consultar:')

if Validations.capital_letter(country_name): # Si el nombre del pais no empiza con mayuscula
    country_raw_info = Tools.get_info_by_country_name( country_name.capitalize() )
    country_dates_info = Tools.get_clear_vector_info(country_raw_info)
    print(country_dates_info)
else:
    country_raw_info = Tools.get_info_by_country_name(country_name)
    country_dates_info = Tools.get_clear_vector_info(country_raw_info)
    print(country_dates_info)