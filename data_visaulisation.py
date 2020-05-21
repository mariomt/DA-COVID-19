from matplotlib import pyplot as plot
from matplotlib import dates as plot_dates
from datetime import date

plot.style.use('seaborn')

def show_plot_dates(dates_array, country_dates_info):
    date_format = plot_dates.DateFormatter('%b, %d, %Y')

    plot.plot_date(dates_array, country_dates_info, linestyle='solid')
    plot.gcf().autofmt_xdate()
    plot.gca().xaxis.set_major_formatter(date_format)
    plot.title('Casos confirmados de COVID-19')
    plot.xlabel('Tiempo')
    plot.ylabel('Numero de casos')
    plot.tight_layout()
    plot.show()
