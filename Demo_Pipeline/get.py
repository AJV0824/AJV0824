# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Code sources COVID-19 data from Google API and creates a file to be normalized in norm.py

# %% tags=[]
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %% tags=[]
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None


# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
product = {"data": "C:\\Users\\avill\\OneDrive\\Projects\\Data Pipeline\\Demo_Pipeline\\output\\data.csv", "nb": "C:\\Users\\avill\\OneDrive\\Projects\\Data Pipeline\\Demo_Pipeline\\output\\get.ipynb"}


# %% tags=[]
# your code here...
from io import StringIO
import requests
import pandas as pd

from pathlib import Path

url = 'https://storage.googleapis.com/covid19-open-data/v3/latest/epidemiology.csv'

r = requests.get(url)

df = pd.read_csv(StringIO(r.text), 
                dtype=str
                )

df.to_csv(product['data'],
        index=False,
        sep=','
        )
