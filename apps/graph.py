import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px 

def app():
    
    media = st.beta_container()
    image = st.beta_container()
    
    df = pd.read_csv('Books_universe.csv')
    
    with media:
        #Another 1
        st.subheader('Book Release:')
        pup = pd.DataFrame(df['original_publish_year'].value_counts()).head(50)
        st.bar_chart(pup)
        st.markdown(''' The number of books published was at its highest in 2003.  ''')

        #Another1
        st.subheader('Authors and how many Books they wrote:')
        
        author_books = df.groupby('author').count()
        author_books =pd.DataFrame(author_books).sort_values(by=['min_max'],ascending=False)[0:50]
        fig = px.scatter(author_books, x=author_books.index.values, y=author_books.title,
        labels={
                            "x":"Authors",
                            "y":"Number of Books",
                            
                        },color=author_books.index
                        )

        fig.update_traces(marker=dict(size=12,
                                    line=dict(width=1,
                                                )),
                        selector=dict(mode='markers'))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False )
        fig.update(layout_showlegend=False)
        fig.update_layout(plot_bgcolor="black",
            height=500,
            title_text='Number of Awards Won by an Individual Author'
        )
        
        st.plotly_chart(fig)
        st.markdown(''' **Stephen King** and **William Shakespeare** clearly were not experiencing 
        any writers block.''')

        #Another1
        st.subheader('Number of Awards:')
        authors = df.groupby(['author'])['award_number'].count()
        authors =pd.DataFrame(authors)
        authors = authors.sort_values(by=['award_number'],ascending=False)[0:50]
        fig = px.bar(authors, x=authors.index.values, y=authors.award_number,color_continuous_scale='agsunset',
        labels={
                            "x":"Authors",
                            "y":"Award Count" }
                        )

        fig.update_traces(marker=dict(size=12,
                                    line=dict(width=1
                                                )),
                        selector=dict(mode='markers'))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False )
        fig.update(layout_showlegend=False)

        fig.update_layout(plot_bgcolor="black",
            height=800,width=800,
            title_text='Number of Awards Won by an Individual Author(Top 50 Authors)')
        st.plotly_chart(fig)

        ##Another 1
        st.subheader('Number of Awards:')
        dx=df.sort_values(by=('min_max'), ascending= False)[0:100]
        fig = px.scatter(dx, x=dx["min_max"].values, y=dx["num_ratings"], hover_name=dx["title"],size=dx['num_pages']*10000, 
        hover_data=['num_pages','author'],labels={
                            "x":"Average Ratings",
                            "y":"Number of Ratings",
                            
                        },color=dx["author"])

        #fig.update_traces(marker=dict(size=df['num_pages']/15))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False )
        fig.update(layout_showlegend=False)
        fig.update_layout(plot_bgcolor="black", height= 1000,width=1400,title_text='Number of Ratings in comparison to the Number of Ratings')
        st.plotly_chart(fig)

        #Another 1
        st.subheader('The Genres:')
        dfclean= df.dropna()

        df_dummy = pd.DataFrame(dfclean.genres.str.split(',',1).tolist(),
                                        columns = ['g1','g2'])
        df_dummy= df_dummy.dropna()


        df2 = pd.DataFrame(df_dummy.g2.str.split(',',1).tolist(),
                                        columns = ['g2','g3'])
        df2= df2.dropna()
        t = []
        for i in df_dummy.g1:
            t.append((i.strip('[').strip(',').strip("''")))
        

        r  = []
        for i in df2.g2:
            r.append((i.strip('[').strip(',').strip("'").strip(" '"))) 
        
    

        s  = []
        for i in df2.g3:
            s.append((i.strip(']').strip(',').strip("'").strip(" '")))
        from collections import Counter
        z= t +r + s
        dfsecond= pd.DataFrame({"Genre": Counter(z).keys(), 
                                "counts": Counter(z).values()})
        dfsecond= dfsecond[:10]
        fig = px.bar(dfsecond, x= "Genre", y= "counts", barmode="group", hover_name=dfsecond["Genre"]
                            , color="Genre",labels={
                            "Genre":"Genre category",
                            "counts":"Number of Books",
                            
                        })
        fig.update_layout(plot_bgcolor="black",height=400, width= 800, title_text='Genres')
        fig.update(layout_showlegend=False)
        for data in fig.data:
            data["width"] = 0.4
        st.plotly_chart(fig)

        st.subheader('The authors:')
        r_books = df.groupby(['author','title'])['num_reviews'].quantile(0.9)
        r_books =pd.DataFrame(r_books).sort_values(by=['num_reviews'],ascending=False)[0:50]
        r_books= r_books.reset_index()
        
        fig = px.bar(r_books, x="author", y="num_reviews", hover_name="title", 
        #hover_data=['num_pages','author'],
        labels={
                            "x":"Author",
                            "y":"Number of reviews",
                            
                        },color="author")

        #fig.update_traces(marker=dict(size=df['num_pages']/15))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False )
        fig.update(layout_showlegend=False)
        fig.update_layout(plot_bgcolor="black",height=500,title_text='Top 50 Most Reviewed books')
        st.plotly_chart(fig)


    

    
app()