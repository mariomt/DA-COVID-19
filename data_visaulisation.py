from matplotlib import pyplot as plot
from matplotlib import dates as plot_dates
from datetime import date
import Tools

# Variables globales
scale       = 1.1
date_format = plot_dates.DateFormatter('%b, %d, %Y')

plot.style.use('seaborn') # Estilo de grafica

def show_all_country_info(dates_array, confirmed_cases, recovered_cases, deaths_cases, country_name):
    # Devuelve una grafica con los casos confirmados, recuperados y decesos de COVID-19 de un 
    # país dado por el usuairo.
    # dates_array: Es un arreglo de fechas de tipo date
    # confirmed_cases: Es un arreglo de enteros que contiene la información de los casos confirmados
    # recovered_cases: Es un arreglo de enteros que contiene la información de los casos recuperados
    # deaths_cases: Es un arreglo de enteros que contiene la información de los decesos
    # country_name: Es el nombre del país.
    active_cases = get_active_cases(confirmed_cases, recovered_cases, deaths_cases)
    current_info = len(dates_array)-1

    # Información de la ultima fecha
    confirmed = confirmed_cases[current_info]
    recovered = recovered_cases[current_info]
    deaths    = deaths_cases[current_info]
    actives   = active_cases[current_info]

    # Calculando porsejantes 
    recovered_rate = (recovered / confirmed)*100
    death_rate     = (deaths / confirmed)*100
    active_rate    = (actives / confirmed)*100

    # Redondenando porsentajes
    recovered_rate = round(recovered_rate, 2)
    death_rate     = round(death_rate, 2)
    active_rate    = round(active_rate, 2)

    # Imprimiendo información de grafica
    print('\n --- --- ' + country_name + ' --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(confirmed) + 
          '\n Casos activos actualmente: {:,}'   .format(actives) + 
          '\n Casos recuperados acumulados: {:,}'.format(recovered) + 
          '\n Decesos acumulados: {:,}'          .format(deaths) + 
          '\n Indice de mortalidad: '            + str(death_rate) + '%' +
          '\n Indice de recuperación: '          + str(recovered_rate) + '%' +
          '\n Indice de casos activos: '         + str(active_rate) + '%')

    # Graficación de información
    plot.plot(dates_array, confirmed_cases, linestyle='solid', color='red', label='Confirmados')
    plot.plot(dates_array, recovered_cases, linestyle='solid', color='green', label='Recuperados')
    plot.plot(dates_array, deaths_cases, linestyle='solid', color='black', label='Muertes')
    ax = plot.plot(dates_array, active_cases, linestyle='solid', color='yellow', label='Activos')
    f  = zoom_factory(ax, base_scale = scale)
    
    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento general de COVID-19 en ' + country_name + ' hasta el ' + str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos')
    plot.tight_layout()
    plot.show()

def get_active_cases(confirmed_cases, recovered_cases, deaths_cases):
    # Devuelve un arreglo con los casos activos
    # confirmed_cases: Es un arreglo de enteros con la información de los casos confirmados.
    # recovered_cases: Es un arreglo de enteros con la información de los casos recuperados.
    # deaths_cases: Es un arreglo de enteros con la información de los decesos.
    array_size = len(confirmed_cases)
    active_cases = []
    
    for n in range(array_size):
        active_cases.append(confirmed_cases[n] - (recovered_cases[n] + deaths_cases[n]))
    
    return active_cases

def show_country_confirmed_cases(dates_array, confirmed_cases, country_name):
    # Grafica y muestra solo la información de los casos confirmados de un país.
    # dates_array: Es un arreglo de fehcas de tipo date.
    # confirmed_cases: Es un arreglo de enteros con los caoss confirmados de un país
    # country_name: Es el nombre del país. 
    current_info = len(dates_array)-1

    # Información de la ultima fecha.
    confirmed = confirmed_cases[current_info]

    # Imprimiendo la información de la grafica
    print('\n --- --- ' + country_name + ' --- ---'
          '\n Casos confirmados acumulados: {:,}'.format(confirmed))

    # Graficación de información
    ax = plot.plot(dates_array, confirmed_cases, linestyle='solid', color='red', label='Casos confirmados')
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos confirmados de COVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos confirmados')
    plot.tight_layout()
    plot.show()

def show_country_recovered_cases(dates_array, recovered_cases, country_name):
    # Grafica y muestra solo los casos recuperados de un país.
    # dates_array: Es un arreglo de fehcas de tipo date.
    # recovered_cases: Es un arreglo de enteros con la información de los casos recuperados de un país.
    # country_name: Es el nombre del país. 
    current_info = len(dates_array)-1

    # Información de la ultima fecha.
    confirmed = Tools.get_confirmed_cases(country_name)
    confirmed = confirmed[current_info]
    recovered = recovered_cases[current_info]

    # Porcentaje de recuperación
    recovered_rate = (recovered / confirmed)*100
    recovered_rate = round(recovered_rate, 4)

    print('\n --- --- ' + country_name + ' --- ---'
          '\n Casos confirmados acumulados: {:,}'.format(confirmed) + 
          '\n Casos recuperados acumulados: {:,}'.format(recovered) +
          '\n Indice de mortalidad: ------> '    + str(recovered_rate) + '%')

    ax = plot.plot(dates_array, recovered_cases, linestyle='solid', color='green', label='Casos recuperados')
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos recuperados de COVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos recuperados')
    plot.tight_layout()
    plot.show()

def show_country_deaths_cases(dates_array, deaths_cases, country_name):
    # Grafica y muestra solo los decesos de un país.
    # dates_array: Es un arreglo de fehcas de tipo date.
    # deaths_cases: Es un arreglo de enteros con la información de los decesos de un país.
    # country_name: Es el nombre del país. 
    current_info = len(dates_array)-1

    # Información de la ultima fecha.
    confirmed = Tools.get_confirmed_cases(country_name)
    confirmed = confirmed[current_info]
    deaths    = deaths_cases[current_info]

    # Pocentaje de mortalidad
    death_rate   = (deaths / confirmed)*100
    death_rate   = round(death_rate, 2)

    print('\n --- --- ' + country_name + ' --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(confirmed) + 
          '\n Decesos acumulados: --------> {:,}'.format(deaths) +
          '\n Indice de mortalidad: ------> '    + str(death_rate) + '%')

    ax = plot.plot(dates_array, deaths_cases, linestyle='solid', color='black', label='Decesos')
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de los decesos por deCOVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de decesos')
    plot.tight_layout()
    plot.show()

def show_country_active_cases(dates_array, confirmed_cases, recovered_cases, deaths_cases, country_name):
    # Grafica y muestra solo los casos activos de un país.
    # dates_array: Es un arreglo de fechas de tipo date
    # confirmed_cases: Es un arreglo de enteros que contiene la información de los casos confirmados
    # recovered_cases: Es un arreglo de enteros que contiene la información de los casos recuperados
    # deaths_cases: Es un arreglo de enteros que contiene la información de los decesos
    # country_name: Es el nombre del país.
    current_info = len(dates_array)-1

    # Información de la ultima fecha.
    active_cases = get_active_cases(confirmed_cases, recovered_cases, deaths_cases)
    confirmed    = confirmed_cases[current_info]
    actives      = active_cases[current_info]

    # Porcentaje de casos activos.
    active_rate = (actives / confirmed)*100
    active_rate = round(active_rate, 4)

    print('\n --- --- ' + country_name + ' --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(confirmed) + 
          '\n Casos activos actualmente: {:,}'   .format(actives) +
          '\n Indice de casos activos: '         + str(active_rate) + '%')

    ax = plot.plot(dates_array, active_cases, linestyle='solid', color='yellow', label='Casos activos')
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos activos de COVID-19 en ' + country_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos activos')
    plot.tight_layout()
    plot.show()

def show_confirmed_vs_countrys(dates_array, confirmed_first_country, confirmed_second_country, first_name, second_name):
    # Grafica y muestra una comparación entre ls casos conformados de 2 paises.
    # dates_array: Es un arreglo de fechas de tipo date.
    # confirmed_first_country: Es un arreglo de enteros con los casos conformados del primer país.
    # confirmed_second_country: Es un arreglo de enteros con los casos conformados del segundo país.
    # first_name: Es el nombre del primer país.
    # second_name: Es el nombre del segundo país.
    current_info = len(dates_array)-1

    # Primer país
    confirmed_1 = confirmed_first_country[current_info]

    # segundo pais
    confirmed_2 = confirmed_second_country[current_info]

    print('\n--- --- ' + first_name + ' --- ---' + ' | --- VS --- |' + '--- --- ' + second_name + ' --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(confirmed_1) + ' |-VS-|-> {:,}'.format(confirmed_2))

    plot.plot(dates_array, confirmed_first_country, linestyle='solid', color='blue', label=first_name)
    ax = plot.plot(dates_array, confirmed_second_country, linestyle='solid', color='green', label=second_name)
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos confirmados de COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos confirmados')
    plot.tight_layout()
    plot.show()

def show_recovered_vs_countrys(dates_array, recovered_first_country, recovered_second_country, first_name, second_name):
    # Grafica y muestra una comparación entre los casos recuperados de 2 paises.
    # dates_array: Es un arreglo de fechas de tipo date.
    # recovered_first_country: Es un arreglo de enteros con los casos recuperados del primer país.
    # recovered_second_country: Es un arreglo de enteros con los casos recuperados del segundo país.
    # first_name: Es el nombre del primer país.
    # second_name: Es el nombre del segundo país.
    current_info = len(dates_array)-1

    # Primer país
    # Información de la ultima fecha del primer país.
    confirmed_1      = Tools.get_confirmed_cases(first_name)
    confirmed_1      = confirmed_1[current_info]
    recovered_1      = recovered_first_country[current_info]

    # Porcentaje de recuperación del primer país.
    recovered_rate_1 = (recovered_1 / confirmed_1)*100
    recovered_rate_1 = round(recovered_rate_1, 4)

    # Segundo país
    # Información de la ulitma fecha del segundo país.
    confirmed_2 = Tools.get_confirmed_cases(second_name)
    confirmed_2 = confirmed_2[current_info]
    recovered_2  = recovered_second_country[current_info]

    # porcentaje de recuperación del segundo país.
    recovered_rate_2 = (recovered_2 / confirmed_2)*100
    recovered_rate_2 = round(recovered_rate_2, 4)

    print('\n--- --- ' + first_name + ' --- ---' + ' | --- VS --- |' + '--- --- ' + second_name + ' --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(confirmed_1) + ' |-VS-|-> {:,}'.format(confirmed_2) +
          '\n Casos recuperados acumulados: {:,}'.format(recovered_1) + ' |-VS-|-> {:,}'.format(recovered_2) +
          '\n Indice de recuperación: ----> ' + str(recovered_rate_1) + '%'    + ' |-VS-|-> ' + str(recovered_rate_2) + '%')

    plot.plot(dates_array, recovered_first_country, linestyle='solid', color='blue', label=first_name)
    ax = plot.plot(dates_array, recovered_second_country, linestyle='solid', color='green', label=second_name)
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos recuperados de COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos recuperados')
    plot.tight_layout()
    plot.show()

def show_deaths_vs_countrys(dates_array, deaths_first_country, deaths_second_country, first_name, second_name):
    # Grafica y muestra una comparación de entre los decesos de 2 paises.
    # dates_array: Es un arreglo de fechas de tipo date.
    # deaths_first_country: Es un arreglo de enteros con los decesos del primer país.
    # deaths_second_country: Es un arreglo de enteros con los decesos del segundo país.
    # first_name: Es el nombre del primer país.
    # second_name: Es el nombre del segundo país.
    current_info = len(dates_array)-1

    # Primer país
    # Información de la ultima fecha del primer país.
    confirmed_1 = Tools.get_confirmed_cases(first_name)
    confirmed_1 = confirmed_1[current_info]
    deaths_1    = deaths_first_country[current_info]

    # Porcentaje de mortalidad del primer país.
    death_rate_1 = (deaths_1 / confirmed_1)*100
    death_rate_1 = round(death_rate_1, 2)

    # Segundo país
    # Información de la ultima fehca del primer país.
    confirmed_2 = Tools.get_confirmed_cases(second_name)
    confirmed_2 = confirmed_2[current_info]
    deaths_2    = deaths_second_country[current_info]

    # Porcentaje de mortalidad del segundo país.
    death_rate_2 = (deaths_2 / confirmed_2)*100
    death_rate_2 = round(death_rate_2, 2)

    print('\n--- --- ' + first_name + ' --- ---' + ' | --- VS --- |' + '--- --- ' + second_name + ' --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(confirmed_1)  + ' |-VS-|-> {:,}'.format(confirmed_2) +
          '\n Decesos acumulados: --------> {:,}'.format(deaths_1)     + ' |-VS-|-> {:,}'.format(deaths_2) +
          '\n Indice de mortalidad: ------> '+ str(death_rate_1) + '%'    + ' |-VS-|-> ' + str(death_rate_2) + '%')

    plot.plot(dates_array, deaths_first_country, linestyle='solid', color='blue', label=first_name)
    ax = plot.plot(dates_array, deaths_second_country, linestyle='solid', color='green', label=second_name)
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de decesos por COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de decesos')
    plot.tight_layout()
    plot.show()

def show_active_vs_countrys(dates_array, first_name, second_name):
    # Grafica y muestra una comparación entre los casos a0ctivos entre 2 paises.
    # dates_array: Es un arreglo de fechas de tipo date.
    # first_name: Es el nombre del primer país.
    # second_name: Es el nombre del segundo país.
    # Obteniendo los daros de los casos confirmados, recuperados y decesos de ambos paises.
    first_confirmed, first_recovered, first_deaths    = Tools.get_info_by_country_name(first_name)
    first_confirmed, first_recovered, first_deaths    = Tools.get_clear_vector_info(first_confirmed, first_recovered, first_deaths)
    second_confirmed, second_recovered, second_deaths = Tools.get_info_by_country_name(second_name)
    second_confirmed, second_recovered, second_deaths = Tools.get_clear_vector_info(second_confirmed, second_recovered, second_deaths)

    # Casos confirmados
    active_first_country  = get_active_cases(first_confirmed, first_recovered, first_deaths)
    active_second_country = get_active_cases(second_confirmed, second_recovered, second_deaths)

    current_info = len(dates_array)-1

    # Primer país
    # Información de la ultima fecha del primer país.
    num_confirmed_1 = first_confirmed[current_info]
    num_active_1    = active_first_country[current_info]

    # Porcentaje de casos activos del primer país.
    active_rate_1   = (num_active_1 / num_confirmed_1)*100
    active_rate_1   = round(active_rate_1, 4)

    # Segundo país
    # Información de la ultima fecha del segundo país.
    num_confirmed_2 = second_confirmed[current_info]
    num_active_2    = active_second_country[current_info]

    # Porcentaje de casos activos del segundo país
    active_rate_2   = (num_active_2 / num_confirmed_2)*100
    active_rate_2   = round(active_rate_2, 4)

    print('\n--- --- ' + first_name + ' --- ---' + ' | --- VS --- |' + '--- --- ' + second_name + ' --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(num_confirmed_1)  + ' |-VS-|-> {:,}'.format(num_confirmed_2) +
          '\n Casos activos actualmente: -> {:,}'.format(num_active_1)     + ' |-VS-|-> {:,}'.format(num_active_2) +
          '\n Indice de casos activos: ---> '+ str(active_rate_1) + '%'    + ' |-VS-|-> ' + str(active_rate_2) + '%')

    plot.plot(dates_array, active_first_country, linestyle='solid', color='blue', label=first_name)
    ax = plot.plot(dates_array, active_second_country, linestyle='solid', color='green', label=second_name)
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento de casos activos de COVID-19 ' + first_name + ' VS. ' + second_name + ' hasta el ' + 
                str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos activos')
    plot.tight_layout()
    plot.show()

def show_global_state(dates_array, confirmed_cases, recovered_cases, deaths_cases):
    # Imprime una lista de todos los paises disponibles en la base de datos.    
    # dates_array: Es un arreglo de fechas de tipo date.
    # confirmed_cases: Es un arreglo de enteros con la información global de los casos confirmados del dataset.
    # recovered_cases: Es un arreglo de enteros con la información global de los casos recuperados del dataset.
    # deaths_cases: Es un arreglo de enteros con la información global de los decesos del dataset.
    active_cases = get_active_cases(confirmed_cases, recovered_cases, deaths_cases)
    current_info = len(dates_array)-1

    # Información de la ultima fecha.
    num_confirmed_cases = confirmed_cases[current_info]
    num_recovered_cases = recovered_cases[current_info]
    num_deaths_cases    = deaths_cases[current_info]
    num_active_cases    = active_cases[current_info]
    
    # Procentajes de mortalidad, recuperación y casos activos
    death_rate     = (num_deaths_cases / num_confirmed_cases)*100 
    recovered_rate = (num_recovered_cases / num_confirmed_cases)*100
    active_rate    = (num_active_cases / num_confirmed_cases)*100
    # total          = death_rate + recovered_rate + active_rate
    death_rate     = round(death_rate, 2)
    recovered_rate = round(recovered_rate, 2)
    active_rate    = round(active_rate, 2)

    print('\n --- --- INFORMACIÓN GLOBAL --- ---' +
          '\n Casos confirmados acumulados: {:,}'.format(num_confirmed_cases) + 
          '\n Casos activos actualmente: {:,}'   .format(num_active_cases) + 
          '\n Casos recuperados acumulados: {:,}'.format(num_recovered_cases) + 
          '\n Decesos acumulados: {:,}'          .format(num_deaths_cases) + 
          '\n Indice de mortalidad: '            + str(death_rate) + '%' +
          '\n Indice de recuperación: '          + str(recovered_rate) + '%' +
          '\n Indice de casos activos: '         + str(active_rate) + '%')

    # Grafica
    plot.plot(dates_array, confirmed_cases, linestyle='solid', color='red', label='Confirmados')
    plot.plot(dates_array, recovered_cases, linestyle='solid', color='green', label='Recuperados')
    plot.plot(dates_array, deaths_cases, linestyle='solid', color='black', label='Decesos')
    ax = plot.plot(dates_array, active_cases, linestyle='solid', color='yellow', label='Activos')
    f  = zoom_factory(ax, base_scale = scale)

    # Estructura
    plot.legend(loc=2)
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Comportamiento global de COVID-19 ' + ' hasta el ' + str(dates_array[ len(dates_array)-1 ]))
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos')
    plot.tight_layout()
    plot.show()

def show_martality_bars(dict_death_rates):
    death_rates = []
    countrys    = []

    for country, death_rate in dict_death_rates.items():
        countrys.append(country)
        death_rates.append(death_rate)

    xmax  = 15
    ymax  = max(death_rates)
    ax    = plot.bar(countrys, death_rates)
    f     = zoom_factory(ax, base_scale = scale)

    plot.gcf().autofmt_xdate()
    plot.axis([0, xmax, 1, ymax])
    plot.show()
      
def zoom_factory(ax,base_scale = 2.):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim   = plot.gca().get_xlim()
        cur_ylim   = plot.gca().get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*.5
        xdata      = event.xdata # get event x location
        ydata      = event.ydata # get event y location

        if event.button == 'down':
            # deal with zoom in
            scale_factor = 1/base_scale
        elif event.button == 'up':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            # print(event.button)

        # set new limits
        plot.gca().set_xlim([xdata - (xdata-cur_xlim[0]) / scale_factor, xdata + 
                             (cur_xlim[1]-xdata) / scale_factor])
        plot.gca().set_ylim([ydata - (ydata-cur_ylim[0]) / scale_factor, ydata + 
                             (cur_ylim[1]-ydata) / scale_factor])
        plot.draw() # force re-draw

    # attach the call back
    plot.gcf().canvas.mpl_connect('scroll_event', zoom_fun)

    #return the function
    return zoom_fun
            