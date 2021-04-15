
import streamlit as st
from multiapp import MultiApp
from apps import about, data # import your app modules here

app = MultiApp()

st.title(' Ravenclaw Team welcomes you to our website')
st.text('')
st.text('')
st.text('')
st.markdown("![Alt Text](https://media4.giphy.com/media/lKYMj63WqlBcc/giphy.gif?cid=ecf05e470d15qsjwvus5fhfgb3l2hpf5js7gqr26lshesrpe&rid=giphy.gif&ct=g)")



st.markdown('''
# Book Project

Please select a page:

''')

# Add all your application here
app.add_app("Home", about.app)
app.add_app("Data", data.app)

# The main app
app.run()

