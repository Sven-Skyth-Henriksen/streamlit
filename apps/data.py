import streamlit as st
import pandas as pd
from PIL import Image

def app():
    
    data = st.beta_container()
    

    df = pd.read_csv('Books_universe.csv')

    with data:
        st.title('Data')
        st.markdown("![Data](https://media4.giphy.com/media/xT9C25UNTwfZuk85WP/200.webp?cid=ecf05e47844brv5239cczg9hqo5ernebyirvx4xaua7k2dk8&rid=200.webp&ct=g)")
        if st.checkbox('View Data'):
            st.subheader('Raw Data')
            st.write(df) #.header(50) inside the the ()


    
    

    
       
    