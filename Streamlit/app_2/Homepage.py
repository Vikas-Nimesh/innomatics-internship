import streamlit as st
import pandas as pd
import numpy as np

app_name = 'Open Pub'

st.set_page_config(page_title=app_name,page_icon='🍷')

st.header('🍷 Welcome to Open Pubs')

df = pd.read_csv('data/cleaned_open_pubs.csv')

total_num_of_pubs = df.shape[0]

top_5_max_pubs_by_local_authority = df.groupby('local_authority').count()['name'].sort_values(ascending=False).head()


st.title('🔢 Total Pubs: {}'.format(total_num_of_pubs))

st.subheader('🔝 Top 5 local authority of having maximum pubs')
st.dataframe(top_5_max_pubs_by_local_authority)
