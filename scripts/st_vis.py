import streamlit as st
from datetime import datetime,date
from helper import *
import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
import time
import numpy as np


# read df for plotly
# ../data/test_df.pkl
df = pack(file_name='data/test_df.pkl',mode='rb')
# la	lo	hover	date_belong location  raw_location
# st.write(df.head())
# plot_spot = st.empty()
# date range slider 
date_list = []
for i in df['date_belong'].tolist():
    date_list.append(string_to_date(i))# date(*[int(j) for j in i.split('-')]))
df['date_belong'] = date_list
date_list = sorted(date_list)

# plot_spot = st.empty()

# date_range = st.slider(
#     "select date range or point:",
#     value=(date_list[0], date_list[-1]))

# st.write(date_range)

# select_date = []
# for i in date_list:
#     if (i <= date_range[1]) & (i >= date_range[0]):
#         select_date.append(i)

# st.write(select_date)

st.title("Plotly Graphs with containers")

t = [[-0.27690107, -0.66460628, -0.48785013],
       [ 0.46648412,  0.83710529,  0.29954414],
       [ 0.16235711,  0.93161425, -1.25728337],
       [ 0.61315424,  0.27982038,  1.12244805],
       [ 0.87584227, -0.19043014, -0.74421412],
       [ 0.77320702,  0.19002869,  1.34489272],
       [-0.26689168,  0.29891508,  0.16287385],
       [ 0.36614639, -0.02249117,  0.14131207],
       [-0.07281827,  0.10335234, -0.11817513],
       [ 0.21812794, -0.28468305,  1.24383485],
       [ 0.77878036,  1.30638707,  0.16946626],
       [-0.05973788, -0.61481474, -1.85956055],
       [ 0.45645592, -0.90021577,  0.79963772],
       [ 0.41952415,  0.77728393,  0.10610808],
       [ 0.09186997, -0.91016074, -0.43602524],
       [-0.78327345, -0.10805522,  0.85692596],
       [ 1.33146707,  0.34060621, -0.92975188],
       [ 0.37900939,  0.67887458, -1.56281853],
       [-0.38229831, -0.554858  ,  0.53029812],
       [-0.03268027,  0.48735482,  0.32412867]]
chart_data = pd.DataFrame(t,columns=['a', 'b', 'c'])

plot_spot = st.empty() # holding the spot for the graph

#make the widgets that will change the graph
line = st.selectbox("Choose a column:", chart_data.columns)
date_range = st.slider(
    "select date range or point:",
    value=(-2, 2))
title = st.radio("Decide to include a title:", ["Yes", "No"])

#now code the plotly chart based on the widget selection
chart_data_ = chart_data.loc[chart_data[line].isin(date_range),:]
fig = px.line(chart_data_, x=chart_data_.index, y=line)

if title == "Yes":
    fig.update_layout(title="My graph title")

#send the plotly chart to it's spot "in the line" 
with plot_spot:
    st.plotly_chart(fig)

def vis(se):
    df_select = df.loc[df['date_belong'].isin(se)]
    d = go.Scattermapbox(lat = df_select['la'],
                            lon = df_select['lo'],
                            mode='markers',
                            marker = dict(size=12,color='black'), # go.scattermapbox.Marker
                            text = df_select['hover'].tolist(),
                            # name = str(i),
                            hoverinfo='text')

    Fig = go.Figure(d)
    Fig.update_layout(mapbox=dict(style='open-street-map',
                                center=dict(lat=52.3,lon=4.9),
                                zoom=5
                                ),
                      margin={"r":0,"t":0,"l":0,"b":0},
                      legend=dict(y=0.2,x=1)
                                )


    st.write(date_range)
    st.write(se)
    st.write(Fig.data)
    with plot_spot:
        st.plotly_chart(Fig)

# vis(select_date)

# # Fig.write_html('test.html')
# st.plotly_chart(Fig)


# if __name__ == "__main__":
#     # pass
#     # st.write('You selected:', chronicle_select)
#     # st.write("date range: ", date_range)
#     print('*********************************************************')