import streamlit as st
import pandas as pd
from PIL import Image

def app():
    data = st.beta_container()
    media = st.beta_container()
    image = st.beta_container()

    df = pd.read_csv('Books_total.csv')

    with data:
        st.title('Data')
        st.markdown("![Data](https://media4.giphy.com/media/xT9C25UNTwfZuk85WP/200.webp?cid=ecf05e47844brv5239cczg9hqo5ernebyirvx4xaua7k2dk8&rid=200.webp&ct=g)")
        if st.checkbox('View Data'):
            st.subheader('Raw Data')
            st.write(df.head(50))

    
    with media:
        st.subheader('Book Release:')
        pup = pd.DataFrame(df['1st Pub'].value_counts()).head(50)
        st.bar_chart(pup)
        st.markdown(''' The release in 2003 is the highst.  ''')

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
  
        st.header('EDA')
        st.markdown(''' Checking the **Correlation** between ***number of pages of the book*** and the ***average
                    ratings*** of it.
                    Exploring whether the average ratings 
                    given has anything to do with the thickness of the book
                ''')

        st.subheader('')
        image = Image.open('plot4.jpeg')
        st.image(image, caption='')
        st.markdown('''
        We can deduce from the very helpfull graph that from the Top 100 books in the sample that the number of pages does indeed affect the average ratings. Firstlly we can note that there are more books that have fewer than 1000 pages in the Top100 and that the min rating is 3.4. However as we gather more data, we would be able to tell a more concrete story.
        ''')
    
        st.subheader('')
        image = Image.open('plot5.jpeg')
        st.image(image, caption='')
    
    