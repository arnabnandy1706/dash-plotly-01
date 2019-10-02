import pandas as pd
import mysql.connector

dbconn = mysql.connector.connect(
  host="localhost",
  user="dbuser",
  passwd="App@123",
  database="disaster"
)

cursor = dbconn.cursor()


CSV = "C:\\Users\\arnabnandy1\\Documents\\Python Projects\\DashPlotly\\DemoCode01\\deaths-natural-disasters.csv"
data = pd.read_csv(CSV, header=0, delimiter=',')
dataFrame = data.fillna(0)

for index, row in dataFrame.iterrows():
    Query = """INSERT INTO disaster.deaths (
        CountryCode, 
        CountryName, 
        YEAR_2019, 
        YEAR_2018, 
        YEAR_2017, 
        YEAR_2016, 
        YEAR_2015, 
        YEAR_2014, 
        YEAR_2013, 
        YEAR_2012, 
        YEAR_2011, 
        YEAR_2010) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    Values = (
        row['CountryCode'], 
        row['CountryName'], 
        row['2019'], 
        row['2018'], 
        row['2017'], 
        row['2016'], 
        row['2015'], 
        row['2014'], 
        row['2013'], 
        row['2012'], 
        row['2011'], 
        row['2010']
    )
        
    
    print(Query, Values)
    cursor.execute(Query, Values)

    dbconn.commit()


    