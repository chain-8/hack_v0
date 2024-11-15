#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries and declare variables

import requests
import os
import pandas as pd
from dotenv import load_dotenv
from dash import Dash, html, dash_table, dcc

load_dotenv()
FMP_API_KEY = os.getenv("FMP_API_KEY")


# In[3]:


#print(FMP_API_KEY)


# In[4]:


#fetch data from api and store it in df

url = f"https://financialmodelingprep.com/api/v3/symbol/available-indexes?apikey={FMP_API_KEY}"
response=requests.get(url)

data = response.json()
#print(data)


# In[5]:


df = pd.DataFrame(data)
#print(df)


# In[6]:


#applayout

app = Dash()
app.layout = html.Div([
    html.Header(
        html.H1("Heading")
    ),

    dcc.Tabs([

        dcc.Tab(
            label="Tab 1"
        ),
        dcc.Tab(
            label="Tab 2"
        ),
        dcc.Tab(
            label="Tab 3"
        )


        
    ]),

    html.Div()

    
],
id="main container",                       
style={
    "backgroundColor": "black",
    "color": "white",
    "border": "2px solid white",
    "width": "100vw",  # Full viewport width
    "height": "100vh",  # Full viewport height
    "display": "flex",
    "flexDirection": "column"
})


# In[7]:


#run application

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
