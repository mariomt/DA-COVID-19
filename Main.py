import Tools
import Validations
import data_visaulisation as plot

# Tools.show_all_countrys()
country_name = input('Ingrese el nombre del pais que desea consultar:')

# Si el nombre del pais no empiza con mayuscula o el campo esta vacio
if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
    country_name = country_name.capitalize()


raw_confirmed, raw_recovered, raw_deaths = Tools.get_info_by_country_name(country_name)
confirmed_cases, recovered_cases, deaths_cases, dates = Tools.get_clear_vector_info(raw_confirmed, raw_recovered, raw_deaths)
plot.show_plot_dates(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)