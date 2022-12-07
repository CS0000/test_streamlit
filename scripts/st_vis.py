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

date_range = st.slider(
    "select date range or point:",
    value=(date_list[0], date_list[-1]))

# st.write(date_range)

select_date = []
for i in date_list:
    if (i <= date_range[1]) & (i >= date_range[0]):
        select_date.append(i)

# st.write(select_date)

st.title("Plotly Graphs with containers")

chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])

plot_spot = st.empty() # holding the spot for the graph

#make the widgets that will change the graph
line = st.selectbox("Choose a column:", chart_data.columns)

title = st.radio("Decide to include a title:", ["Yes", "No"])

#now code the plotly chart based on the widget selection
fig = px.line(chart_data, x=chart_data.index, y=line)

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