# Code and artifact reference

[Overview](../README.md) · [Walkthrough](PROJECT_GUIDE.md) · [Development guide](DEVELOPMENT.md)

This reference describes the files on this branch. Function names are navigation aids; the walkthrough explains how their inputs, state, and outputs fit together.

## Python modules

### [dashboard.py](../dashboard.py)

Join GDP and unemployment records by date and write a two-series Bokeh HTML chart.

- `make_dashboard(x, gdp_change, unemployment, title, file_name)`
- `build_dashboard(gdp_csv, unemployment_csv, output)`

## Notebooks

| File | Responsibility |
| --- | --- |
| [Jupyter.ipynb](../Jupyter.ipynb) | Historical data/dashboard exercise, including an explicitly opt-in cloud-export section. |
| [Panda.ipynb](../Panda.ipynb) | pandas spreadsheet/dataframe practice; Excel work uses openpyxl. |

Notebook outputs and credentials are not application configuration. Use environment-provided credentials only when deliberately enabling cloud export.

## Checks and setup

[Tests](../tests/) contains the focused checks described in the [development guide](DEVELOPMENT.md). Consult that guide for dependencies, commands, and the boundary between automated validation and untested integrations.
