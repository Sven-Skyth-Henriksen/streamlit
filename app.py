
import streamlit as st
from multiapp import MultiApp
from apps import about, data, home, graph  # import your app modules here

app = MultiApp()

header = st.beta_container()
meme = st.beta_container()
sub = st.beta.container()
sel = st.beta.container()



with header:
    st.title(' Ravenclaw Team welcomes you to our website')
   
    
with meme:
    st.markdown("![Alt Text](https://media4.giphy.com/media/lKYMj63WqlBcc/giphy.gif?cid=ecf05e470d15qsjwvus5fhfgb3l2hpf5js7gqr26lshesrpe&rid=giphy.gif&ct=g)")


with sub:
    st.markdown('## 🔥 Best books you really have to read once 🔥 ')

with sel:
    st.markdown('Please select a page:')

# Add all your application here
app.add_app('Home',home.app)
app.add_app("About", about.app)
app.add_app("Data", data.app)

app.add_app('Graphs', graph.app)



# The main app
app.run()

