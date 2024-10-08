import streamlit as st
import pandas as pd
import numpy as np


st.title('Transport Claim Irregularities')

  
DATA_URL = ('https://raw.githubusercontent.com/ngalp/auditscribe/refs/heads/main/data/data.csv')

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
data = load_data(DATA_URL)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Value of Claims by Number of Trips')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)
st.scatter_chart(data=data, x="Count", y="Value", x_label="Count", y_label="Value")

# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)