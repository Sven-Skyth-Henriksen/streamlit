import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import pages.about


header = st.beta_container()
image = st.beta_container()
data = st.beta_container()
media = st.beta_container()
plot = st.beta_container()


df = pd.read_csv('Books_total.csv')

#Navigation bar
Pages = {
    'Home': pages.Home
}
st.sidebar.title("Navigation")
selection = st.sidebar.radio("To", list(PAGES.keys()))
page = PAGES[selction]

with header:
    st.title('Books That Everyone Should Read At Least Once\n')     

with image:
    image = Image.open('book.jpeg')
    st.image(image, caption='Quote by ERNEST HEMINGWAY')
    
 #Main Part of the Website  
with data:
    if st.checkbox('View Data'):
        st.subheader('Raw Data')
        st.write(df.head(50))

    
    
with media:
    st.subheader('Book Title')
    pup = pd.DataFrame(df['1st Pub'].value_counts()).head(50)
    st.bar_chart(pup)

    st.subheader('Authors and how many Books they wrote')
    author = pd.DataFrame(df['Author'].value_counts()).head(50)
    st.area_chart(author)
    
    #col1.subheader("A wide column with a chart")
    
    #col1.line_chart()

if __name__ == "__main__":
    main()