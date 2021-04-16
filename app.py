from PIL import Image
import streamlit as st
from multiapp import MultiApp
from apps import about, data, home, graph  # import your app modules here

app = MultiApp()



st.markdown("![Alt Text](https://media4.giphy.com/media/lKYMj63WqlBcc/giphy.gif?cid=ecf05e470d15qsjwvus5fhfgb3l2hpf5js7gqr26lshesrpe&rid=giphy.gif&ct=g)")


st.title(' Ravenclaw Team welcomes you to our website')
st.text('--------------------------------------------- ')
st.text(' ')
st.text(' ')

st.markdown(' ')
st.markdown('## 🔥 Best books you really have to read once 🔥 ')
st.markdown('----------------------------------------------- ')
st.markdown(' ')
st.markdown('Please select a page:')

# Add all your application here
app.add_app('Home',home.app)
app.add_app("About", about.app)
app.add_app("Data", data.app)

app.add_app('Graphs', graph.app)



# The main app
app.run()

