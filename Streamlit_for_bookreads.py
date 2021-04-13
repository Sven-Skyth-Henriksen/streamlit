import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser

header = st.beta_container()
media = st.beta_container()




with header:
    st.title('Books That Everyone Should Read At Least Once\n \n')
    st.text('')
    st.markdown('## About ⬇️⬇️⬇️⬇️: ')
    
    st.write('''This is a Project from 4 [Strive School](https://strive.school/) Students who where scraping some book-datas from
             a website called goodreads.com''')
    
    
    st.markdown('## Get to know us 👋🏻:')
    

    if st.button('Click here'):
        st.write('• Sven Skyth Henriksen: [GitHub](https://github.com/Sven-Skyth-Henriksen)&[LinkedIn](https://www.linkedin.com/in/sven-skyth-henriksen-4857bb1a2/)')
        st.write('• Madina: [GitHub]()&[LinkedIn]()')
        st.write('• Olatunde Salami: [GitHub](https://github.com/salamituns)&[LinkedIn](https://www.linkedin.com/in/olatunde-salami/)')
        st.write('• Paramveer Singh: [GitHub](https://github.com/paramveer)&[LinkedIn](https://www.linkedin.com/in/paramveer-singh07/)')
    else:
        st.write('Goodbye')
    st.text('')
    df = pd.read_csv('BooksThatEveryoneSho.csv')
    st.write(df.head(50))

    
    
with media:
    st.text('Title')
    title = pd.DataFrame(df['title'].value_counts()).head(50)
    st.bar_chart(title)

    st.text('Title')
    title = pd.DataFrame(df['title'].value_counts()).head(50)
    st.area_chart(title)
    
    st.text('Avg_Ratings')
    title = pd.DataFrame(df['avg_ratings'].value_counts()).head(50)
    st.line_chart(avg_ratings,width = 100,height =100)
