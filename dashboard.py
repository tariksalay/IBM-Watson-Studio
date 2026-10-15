"""Create a local Bokeh dashboard without an IBM account or implicit uploads."""
import argparse
from pathlib import Path

import pandas as pd
from bokeh.plotting import figure, output_file, save


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    if not (len(x) == len(gdp_change) == len(unemployment)):
        raise ValueError('Dates and metric series must have equal lengths.')
    plot = figure(title=title, x_axis_label='year', y_axis_label='%')
    plot.line(x, gdp_change, color='firebrick', line_width=4, legend_label='% GDP change')
    plot.line(x, unemployment, line_width=4, legend_label='% unemployed')
    output_file(str(file_name), title=title)
    save(plot)
    return plot


def build_dashboard(gdp_csv, unemployment_csv, output):
    gdp = pd.read_csv(gdp_csv)
    unemployment = pd.read_csv(unemployment_csv)
    data = gdp[['date', 'change-current']].merge(
        unemployment[['date', 'unemployment']], on='date', how='inner', validate='one_to_one')
    if data.empty:
        raise ValueError('The input files have no matching dates.')
    data = data.sort_values('date')
    return make_dashboard(data['date'], data['change-current'], data['unemployment'],
                          'US economic indicators', output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('gdp_csv', type=Path)
    parser.add_argument('unemployment_csv', type=Path)
    parser.add_argument('--output', type=Path, default=Path('dashboard.html'))
    args = parser.parse_args()
    build_dashboard(args.gdp_csv, args.unemployment_csv, args.output)
