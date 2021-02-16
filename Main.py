import pandas as pd
import numpy as np
from IPython import display
path_to_csv = 'Online Retail_2.csv'

display(pd.read_csv(path_to_csv, usecols=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']))