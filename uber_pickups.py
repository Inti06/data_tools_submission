# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Set the title of your Streamlit app
st.title('Uber pickups in NYC')

# Define constants for the data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Create a function to load the data using st.cache_data decorator
@st.cache_data
def load_data(nrows):
    # Load data from the provided URL and specify the number of rows to load
    data = pd.read_csv(DATA_URL, nrows=nrows)
    
    # Convert column names to lowercase
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    
    # Convert the 'date/time' column to datetime format
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    
    return data

# Display a loading message while loading the data
data_load_state = st.text('Loading data...')
data = load_data(10000)  # Load the first 10,000 rows of data
data_load_state.text("Done! (using st.cache_data)")  # Display a message when data loading is complete

# Create a checkbox to show or hide raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Create a subheader and bar chart to display the number of pickups by hour
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Create a slider to filter data by hour
hour_to_filter = st.slider('hour', 0, 23, 17)  # Default value set to 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# Display a subheader and map with filtered data
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
