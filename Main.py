import pandas as pd
import numpy as np
from IPython.display import display, Markdown
path_to_csv = 'Online Retail_2.csv'

dt = pd.read_csv(path_to_csv, usecols=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])

display(dt)

dt2 = dt['product_type'] = dt['StockCode'].str[0]
print("Fin")