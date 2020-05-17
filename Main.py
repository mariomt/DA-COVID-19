import Tools
import Validations
import data_visaulisation as plot

# Tools.show_all_countrys()
country_name = input('Ingrese el nombre del pais que desea consultar:')

if Validations.capital_letter(country_name): # Si el nombre del pais no empiza con mayuscula
    country_name = country_name.capitalize()

country_raw_info = Tools.get_info_by_country_name(country_name)
country_dates_info, dates = Tools.get_clear_vector_info(country_raw_info)
plot.show_plot_dates(dates, country_dates_info)