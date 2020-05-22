from matplotlib import pyplot as plot
from matplotlib import dates as plot_dates
from datetime import date

plot.style.use('seaborn') # Estilo de grafica

def show_plot_dates(dates_array, confirmed_cases, recovered_cases, deaths_cases, country_name):
    # Devuelve una grafica con los casos confirmados, recuperados y decesos de COVID-19 de un 
    # país dado por el usuairo.
    # dates_array: Es un arreglo de fechas de tipo date
    # confirmed_cases: Es un arreglo de enteros que contiene la información de los casos confirmados
    # recovered_cases: Es un arreglo de enteros que contiene la información de los casos recuperados
    # deaths_cases: Es un arreglo de enteros que contiene la información de los decesos

    # Graficación de información
    plot.plot(dates_array, confirmed_cases, linestyle='solid', color='red', label='Confirmados')
    plot.plot(dates_array, recovered_cases, linestyle='solid', color='green', label='Recuperados')
    plot.plot(dates_array, deaths_cases, linestyle='solid', color='black', label='Muertes')

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    date_format = plot_dates.DateFormatter('%b, %d, %Y')
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de COVID-19 en ' + country_name + ' hasta el ' + str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos')
    plot.tight_layout()
    plot.show()
