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
# ## Normalization process of removing unwanted columns and performing calculations for death rate and revover rate per region.
#
# ## Sends normilized data as extract to target 'prod' folder

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
upstream = ['get']

# This is a placeholder, leave it as None
product = None


# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
upstream = {"get": {"data": "C:\\Users\\avill\\OneDrive\\Projects\\Data Pipeline\\Demo_Pipeline\\output\\data.csv", "nb": "C:\\Users\\avill\\OneDrive\\Projects\\Data Pipeline\\Demo_Pipeline\\output\\get.ipynb"}}
product = {"data": "C:\\Users\\avill\\OneDrive\\Projects\\Data Pipeline\\Demo_Pipeline\\output\\extract.csv", "nb": "C:\\Users\\avill\\OneDrive\\Projects\\Data Pipeline\\Demo_Pipeline\\output\\norm.ipynb"}


# %% tags=[]
# your code here...
from enum import Enum
from pathlib import Path

import pandas as pd
import numpy as np

df = pd.read_csv(upstream['get']['data'],
                dtype = str,
                usecols = ['date','location_key','cumulative_confirmed','cumulative_deceased','cumulative_recovered','cumulative_tested']
                )

death_lam = lambda x: float(x['cumulative_deceased']) / float(x['cumulative_confirmed']) if x['cumulative_confirmed'] != '0' else np.nan
    
recovery_lam = lambda x: float(x['cumulative_recovered']) / float(x['cumulative_confirmed']) if x['cumulative_confirmed'] != '0' else np.nan
    
df['death_rate'] = df[['cumulative_deceased','cumulative_confirmed']].apply(death_lam, axis=1)
    
df['recover_rate'] = df[['cumulative_recovered','cumulative_confirmed']].apply(recovery_lam, axis=1)
    
df.to_csv(product['data'],
        sep = ',',
        index = False
        )
