import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('data/cleaned_open_pubs.csv')

st.title('🍷 Nearest Pubs')

latitude = st.number_input('Enter latitude')
st.write('The current latitude is ', latitude)

longitude = st.number_input('Enter longitude')
st.write('The current longitude is ', longitude)


user_input = [latitude,longitude]


distances = np.sqrt(np.sum((user_input - df[['latitude','longitude']])**2, axis = 1))

min_indices = np.argpartition(distances,5-1)[:5]


st.dataframe(df.iloc[min_indices])
st.map(df.iloc[min_indices])