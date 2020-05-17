from matplotlib import pyplot as plot
from matplotlib import dates as plot_dates
from datetime import date
import numpy as np

plot.style.use('seaborn')

def show_plot_dates(dates_array, country_dates_info):
    dates_array = np.array(dates_array)
    country_dates_info = np.array(country_dates_info)
    plot.plot_date(dates_array, country_dates_info, linestyle='solid')
    plot.tight_layout()
    plot.show()