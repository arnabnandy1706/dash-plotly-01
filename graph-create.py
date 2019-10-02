# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import mysql.connector

dbconn = mysql.connector.connect(
  host="localhost",
  user="dbuser",
  passwd="App@123",
  database="disaster"
)

cursor = dbconn.cursor()

GetQuery = """SELECT * from disaster.deaths;"""

SQL_Query = pd.read_sql_query(GetQuery, dbconn)

dataFrame = pd.DataFrame(
    SQL_Query, 
    columns=[
        'CountryId', 
        'CountryCode', 
        'CountryName', 
        'YEAR_2019', 
        'YEAR_2018', 
        'YEAR_2017', 
        'YEAR_2016', 
        'YEAR_2015', 
        'YEAR_2014', 
        'YEAR_2013', 
        'YEAR_2012', 
        'YEAR_2011', 
        'YEAR_2010', 
        ]
        )

print(dataFrame)

Countries = []
CountryCode = []
Datas = {}
for index, row in dataFrame.iterrows():
    Countries.append(row['CountryName'])

#print(Countries)

Years = list(dataFrame.columns)[3:]
Datas['x'] = Years

#for country in Countries:
    
    #for head in headers:

print(Datas)

data = []

for indx in dataFrame.index:
    '''
    print(
        dataFrame['YEAR_2019'][indx], 
        dataFrame['YEAR_2018'][indx], 
        dataFrame['YEAR_2017'][indx], 
        dataFrame['YEAR_2016'][indx], 
        dataFrame['YEAR_2015'][indx], 
        dataFrame['YEAR_2014'][indx], 
        dataFrame['YEAR_2013'][indx], 
        dataFrame['YEAR_2012'][indx], 
        dataFrame['YEAR_2011'][indx], 
        dataFrame['YEAR_2010'][indx],    
    )
    '''
    Accidents = [
       dataFrame['YEAR_2019'][indx], 
        dataFrame['YEAR_2018'][indx], 
        dataFrame['YEAR_2017'][indx], 
        dataFrame['YEAR_2016'][indx], 
        dataFrame['YEAR_2015'][indx], 
        dataFrame['YEAR_2014'][indx], 
        dataFrame['YEAR_2013'][indx], 
        dataFrame['YEAR_2012'][indx], 
        dataFrame['YEAR_2011'][indx], 
        dataFrame['YEAR_2010'][indx],  
    ]

    
    

    Datas['y'] = Accidents

    Datas['type'] = "line"
    Datas['name'] = dataFrame['CountryName'][indx]
    print(Datas['name'])

    print(Datas)

    data.append(Datas)
    #print(Accidents)

#print(data)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Accidents All oVer the World in Years'),

    html.Div(children='''
        Graph Analysis of Accident over the world from year 2010 - 2019
    '''),

    
    dcc.Graph(
        id='Accident-Graph',
        figure={
            'data': data,
            'layout': {
                'title': 'Accident Analysis'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)