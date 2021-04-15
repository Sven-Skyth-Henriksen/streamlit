import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px 

@st.cache
def load_data():
    data = st.beta_container()
    with data:
        st.title('Data')
        st.subheader('Raw Data')
        df = pd.read_csv('Books_universe.csv')
        df = df.drop(['Unnamed: 0'],axis=1)
        #r_books = df.groupby(['author','title'])['num_reviews'].quantile(0.9)
        #r_books =pd.DataFrame(r_books).sort_values(by=['num_reviews'],ascending=False)[0:50]
        #r_books= r_books.reset_index()
        #dx=df.sort_values(by=('min_max'), ascending= False)[0:200]
        #dx
        st.write(df)
    
    return df

      
df = load_data()

#Sidebar - Author selection
authors = df.groupby(['author'])#['min_max'].mean()
#authors_ratings =pd.DataFrame(authors_ratings).sort_values(by=['min_max'],ascending=False)[0:50]
sorted_authors = sorted(df['author'].unique()) 
selected_author = st.sidebar.selectbox('Author',sorted_authors)

#Slider Selection
#st.subheader("Average Ratings:")
#rating_slider = st.slider("To your heart's content",min_value = df.min_max.min(),max_value=df.min_max.max(),step =0.1)

#Filtering Data
dfx = df[(df.author.str.contains(selected_author))]

st.header('Display Book Universe')
st.write('Data Dimension: ' + str(dfx.shape[0]) + ' rows and ' + str(dfx.shape[1]) + ' columns.')
st.dataframe(dfx)



