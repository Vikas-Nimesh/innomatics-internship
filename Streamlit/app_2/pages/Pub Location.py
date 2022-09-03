import streamlit as st
import pandas as pd

df = pd.read_csv('data/cleaned_open_pubs.csv')

st.title('Pub Locations')

choice = st.radio("Search Pubs by",
     ('Pincode', 'Local Authority'), index=0, disabled=False, horizontal=False)

entered_text = ''



if choice == 'Pincode':
    entered_text = st.text_input('Pincode', )
    st.write('Entered pincode is', entered_text)
    pincode_df = df[df['postcode'] == entered_text].loc[:,['latitude','longitude']]
    st.write('Found ', pincode_df.shape[0],'Pubs')
    st.dataframe(pincode_df)
    st.map(pincode_df)
else:
    entered_text = st.text_input('Local Authority', )
    st.write('Entered Local Authority is', entered_text)
    pincode_df = df[df['local_authority'] == entered_text].loc[:,['latitude','longitude']]
    st.write('Found ', pincode_df.shape[0],'Pubs')
    st.dataframe(pincode_df)
    st.map(pincode_df)




