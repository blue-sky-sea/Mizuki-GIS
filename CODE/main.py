#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:55:39 2021

@author: liuyi
"""
from flask import Flask
import numpy as np
import pandas as pd 

import folium
from folium import plugins 
from folium.plugins import HeatMap

import pandas 
data = pandas.read_csv("COVID-19.csv")

df=data
df = df[['受診都道府県','確定日','X','Y']]
df_1 = df[df['確定日'].str.contains("1/15/2020")]
df = df_1
df  = df.groupby(df.columns.tolist(),as_index=False).size()

data=[]
for i in range(len(df)):
  #print(df.iloc[i])
  pass
  row=df.iloc[i]
  temp=[row["Y"],row["X"],row["size"]]
  data.append(temp)



app = Flask(__name__)


@app.route('/')
def index():
    lat=139
    lng=36
    folium_map = folium.Map(location=[lng, lat], zoom_start=7)
    
    for lat, lon in zip(df.Y, df.X):
        folium.Marker(
            location=[lat, lon],
            popup="/".join([str(lat), str(lon)]),
            tooltip=str(lat) + "_" + str(lon),
        ).add_to(folium_map)


    HeatMap(data).add_to(folium_map)

    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)