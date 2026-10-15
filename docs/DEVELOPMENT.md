# Development and validation

Use Python 3.11 or 3.12 and install `requirements.txt` in an isolated environment. Start JupyterLab to open the two notebooks. The original notebook dataset URLs are external coursework assets and may need replacement if unavailable.

For a local dashboard without cloud credentials:

```sh
python dashboard.py path/to/gdp.csv path/to/unemployment.csv --output dashboard.html
python -m unittest discover -s tests -v
```

The GDP CSV needs `date,change-current`; unemployment needs `date,unemployment`. Dates are joined and checked for uniqueness before plotting. Bokeh uses the current `legend_label` API; Excel loading uses openpyxl. Notebook outputs are cleared to avoid stale results or stored links.

Cloud export is optional and disabled by default. Set `UPLOAD_TO_IBM_CLOUD=1`, `IBM_COS_ENDPOINT`, `IBM_COS_BUCKET`, `IBM_COS_ACCESS_KEY_ID`, and `IBM_COS_SECRET_ACCESS_KEY` only in your local environment. The notebook never prints credentials or presigned links. Previously committed credentials have been removed from the current notebook, but **must be revoked/rotated in IBM Cloud**, because historical commits still contain them. No attempt was made to test, use, or revoke those credentials.

Tests validate notebook structure and executable Python cells, series validation, and date alignment using synthetic local CSV files. Live external datasets and cloud export are not exercised.
