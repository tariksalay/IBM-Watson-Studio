# US Economic Indicators: pandas and Bokeh

**Python · pandas · Jupyter · Bokeh · Data preparation**

A small collection of IBM/Cognitive Class learning exercises, plus a local dashboard script. The main workflow aligns GDP change and unemployment observations by date and produces an interactive Bokeh HTML chart.

## What this project demonstrates

- Reading, filtering, and indexing tabular CSV/Excel data.
- Joining related time-series observations before visualization.
- A local analysis path that works without cloud credentials.

## Start here

| Read | Use it for |
| --- | --- |
| [Project walkthrough](docs/PROJECT_GUIDE.md) | Purpose, workflow, repository map, and a concrete example |
| [Code and artifact reference](docs/CODE_REFERENCE.md) | Important files, functions, classes, and their responsibilities |
| [Development guide](docs/DEVELOPMENT.md) | Setup, configuration, commands, tests, and remaining limitations |

## Explore locally

Use Python 3.11 or 3.12 in a virtual environment.

```sh
python -m pip install -r requirements.txt
python dashboard.py path/to/gdp.csv path/to/unemployment.csv --output dashboard.html
python -m unittest discover -s tests -v
```

Use `jupyter lab` to open the original notebooks after installing the requirements.

## Validation and scope

Four tests pass for notebook structure, executable code cells, embedded-credential patterns, input lengths, and synthetic CSV alignment. Live course-dataset URLs and IBM Cloud export were not tested. These are educational exercises; there is no scheduled refresh or maintained production dashboard.



---

[GitHub profile](https://github.com/tariksalay) · [Portfolio](https://tariksalay.github.io/) · [Earlier README](README_HISTORY.md)

The earlier README is preserved as historical context; the guides above describe this branch's implementation.
