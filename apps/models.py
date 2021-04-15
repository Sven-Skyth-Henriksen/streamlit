import streamlit as st
import pandas as pd
from PIL import Image

def app():
    
    media = st.beta_container()
    image = st.beta_container()
    
    df = pd.read_csv('Books_universe.csv')
    
    with media:
        st.subheader('Book Release:')
        pup = pd.DataFrame(df['1st Pub'].value_counts()).head(50)
        st.bar_chart(pup)
        st.markdown(''' The most books got published in 2003.  ''')

        st.subheader('Authors and how many Books they wrote:')
        author = pd.DataFrame(df['Author'].value_counts()).head(50)
        st.area_chart(author)
        st.markdown('''Here we can see clearly that **Stephen King** and **William Shakespeare**
        published the most books
        ''')
    
        st.subheader('Rating Count:')
        rating_count = pd.DataFrame(df['Rating Count'].value_counts()).head(50)
        st.area_chart(rating_count)
    
    with image:
        st.subheader('Avg-Ratings / Pages')
        image = Image.open('plot1.jpeg')
        st.image(image, caption='')
 
        st.subheader('Avg-Ratings / Author')
        image = Image.open('plot2.jpeg')
        st.image(image, caption='')