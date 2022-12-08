import streamlit as st
from datetime import datetime,date
from helper import *
import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px



# read df for plotly
df = pack(file_name='data/test_df.pkl',mode='rb')

date_list = []
for i in df['date_belong'].tolist():
    date_list.append(string_to_date(i))
df['date_belong'] = date_list
date_list = sorted(date_list)


st.title("Plotly map test")



d1,d2 = st.slider(
    "select date range or point:",
    date_list[0], date_list[-1],value=(date_list[0],date_list[10]))

plot_spot = st.empty()

df_select = df.loc[(df['date_belong']<=d2)&(df['date_belong']>=d1),:]
# df_select.loc[:,'size'] = 6
Fig = px.scatter_mapbox(df_select,
                        lat='la',lon='lo',
                        hover_name='hover',
                        size_max=12,
                        # mapbox_style='open-street-map',
                        # center=dict(lat=52.3,lon=4.9),
                        width=1000,height=600)
# fig = go.Figure(data=go.Scattermapbox(lat = df_select['la'],
#                             lon = df_select['lo'],
#                             mode='markers',
#                             marker = dict(size=12,color='black'), 
#                             text = df_select['hover'].tolist(),
#                             hoverinfo='text'))
Fig.update_layout(mapbox=dict(style='open-street-map',
                  center=dict(lat=52.3,lon=4.9),
                  zoom=5),
                  margin={"r":0,"t":0,"l":0,"b":0},
                      # legend=dict(y=0.2,x=1)
                                )

with plot_spot:
    st.plotly_chart(Fig)




