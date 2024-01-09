# midori


To install the Python library requirements, run
```{sh}
pip install -r requirements.txt
```

To update requirements, modify the libraries in `requirements.in` and run
```{sh}
pip-compile requirements.in
```

To run `data_cleaning.ipynb`, include the desired source `.csv` file located in `csv/`.

To run the app locally, run

```{sh}
streamlit run app.py
```

To set up the MongoDB database, from the repo root,
```{sh}
cd webapp/.streamlit
touch secrets.toml

```
In `secrets.toml`, write your MongoDB username and password in the format (with quotation marks),
```{sh}
mongo_username = "{username}"
mongo_password = "{password}"
```


### Supported Modifications to Web Application


### Miscellaneous

`scripts/` contains Python files and Jupyter Notebooks that can be run on individual CSV (found in `csv/`) and other formats of data to filter and process data as well as generate responses from OpenAI found in their documentation [here](https://platform.openai.com/docs/models).