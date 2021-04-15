import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def app():
    header = st.beta_container()
    image = st.beta_container()

    with header:
        st.title('Books That Everyone Should Read At Least Once\n')     
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.title('⚜️ About ⚜️:')
        st.markdown('''
    
    Books are disponible for everyone, rich and poor, young and old. 
    From love stroies to Sci Fi, it's gonna change the world for 
    everyone. How will your life be affected ?📖
    
   ⬇️⬇️ This Project was created by 4 ***[Strive School](https://strive.school/)*** Students.⬇️⬇️
    ''')
    
        st.markdown('## Get to know us 👋🏻:')

    
        if st.button('Click here'):
            
            st.markdown("![Hello There](https://media2.giphy.com/media/3ornk57KwDXf81rjWM/200w.webp?cid=ecf05e47chobelyn3nvbi5od5v1l7ahhd8t9uy1irct4rqiq&rid=200w.webp&ct=g)")
            st.write('***The Developer Team***:')
            st.write('• Paramveer Singh: [GitHub ](https://github.com/paramveer)&[ LinkedIn](https://www.linkedin.com/in/paramveer-singh07/)')
            st.write('• Sven Skyth Henriksen: [GitHub ](https://github.com/Sven-Skyth-Henriksen)&[ LinkedIn](https://www.linkedin.com/in/sven-skyth-henriksen-4857bb1a2/)')
            st.write('• Madina Zhenisbek: [GitHub ](https://github.com/madinach)&[ LinkedIn](https://www.linkedin.com/in/madina-zhenisbek/)')
            st.write('• Olatunde Salami: [GitHub ](https://github.com/salamituns)&[ LinkedIn](https://www.linkedin.com/in/olatunde-salami/)')
            
            st.text('')
            
            st.markdown("![Book](data:image/jpeg;base64,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)")
        

        
    with image:
        image = Image.open('book.jpeg')
        st.image(image ,caption='Quote by ERNEST HEMINGWAY')