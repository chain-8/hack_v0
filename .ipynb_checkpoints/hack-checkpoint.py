#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import pandas as pd
FMP_API_KEY = os.getenv("FMP_API_KEY")


# In[2]:


#Check
#print(FMP_API_KEY)


# In[3]:


# Stock List --> Available Indexes
url = f"https://financialmodelingprep.com/api/v3/symbol/available-indexes?apikey={FMP_API_KEY}"
response=requests.get(url)


# In[4]:


#Check 

#print(url)
#print(response)
#print(response.json())


# In[5]:


df = pd.DataFrame(response.json())


# In[6]:


#Check

#display(df)


# In[7]:


from dash import Dash, html, dash_table, dcc


# In[8]:


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


# In[9]:


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




