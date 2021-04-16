import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px


def app():

    media = st.beta_container()
    image = st.beta_container()

    df = pd.read_csv('Books_universe.csv')

    with media:
        # Another 1
        with st.beta_expander('• In what year was most of the outstanding books released?'):
            #st.text('Books released')
            st.subheader('Book Release:')
            st.markdown(''' The bar graphs shows the number of books published in a given year starting from 1929 until 2014. 
            The highest number of books was released in 2003. Possibly, it was due to the availability of audiobooks and ebooks on the market. 
            Moreover, it is clear that the number of books released increases mainly throughout the given period of time.  ''')
            pup = pd.DataFrame(df['original_publish_year'].value_counts()).head(50)
                #df['original_publish_year'][1::].value_counts()).head(50)
            pup = pup [1::]
            st.bar_chart(pup)
            

        # Another1

        with st.beta_expander('• Books featured by a single Author'):
            st.subheader('Number of Books by a single Author:')
            st.markdown(''' **Stephen King** and **William Shakespeare** clearly were not experiencing any writers block.''')

            author_books = df.groupby('author').count()
            author_books = pd.DataFrame(author_books).sort_values(
                by=['min_max'], ascending=False)[0:50]
            fig = px.scatter(author_books, x=author_books.index.values, y=author_books.title,
                             labels={
                                 "x": "Authors",
                                 "y": "Number of Books",

                             }, color=author_books.index
                             )

            fig.update_traces(marker=dict(size=12,
                                          line=dict(width=1,
                                                    )),
                              selector=dict(mode='markers'))
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            fig.update(layout_showlegend=False)
            fig.update_layout(plot_bgcolor="black",
                              height=500,
                              title_text='Number of Awards Won by an Individual Author'
                              )

            st.plotly_chart(fig)
            

        # Another1
        with st.beta_expander('• Curious about the most Decorated Authors? Click me!'):
            st.subheader('Number of Awards') 
            st.markdown(''' **Stephen King** and **William Shakespeare** clearly were not experiencing 
            any writers block.On the figure, we can see the number of awards won by an Individual Author for books in our list.
            For people who are interested to read the most award-winning books,
            we recommend checking out Stephen King's and William Shakespeare's books.''')
            
            authors = df.groupby(['author'])['award_number'].count()
            authors = pd.DataFrame(authors)
            authors = authors.sort_values(
                by=['award_number'], ascending=False)[0:50]
            fig = px.bar(authors, x=authors.index.values, y=authors.award_number, color_continuous_scale='agsunset',
                        labels={
                            "x": "Authors",
                            "y": "Award Count"}
                        )

            fig.update_traces(marker=dict(size=12,
                                        line=dict(width=1
                                                    )),
                            selector=dict(mode='markers'))
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            fig.update(layout_showlegend=False)

            fig.update_layout(plot_bgcolor="black",
                            height=800, width=800,
                            title_text='Number of Awards Won by an Individual Author(Top 50 Authors)')
            st.plotly_chart(fig)
            

        # Another 1
        with st.beta_expander('• Thick books can be daunting, right? Let us find out if it really is off-putting...'):
            st.subheader('You are in luck:')
            st.markdown('''We created a beatiful visual for you make an informed decision on whether reading that thick book is worh your time.''')
            st.markdown(''' We analyzed the comparison of a number of ratings to the average ratings of books in the list. 
            The size of the point on the diagram describes the number of pages of a certain book. 
            The first thing to point out is the fact that most of the books have an average rating between **7.0 - 8.5**. 
            The most rated books have the lowest number of ratings. 
            Secondly, we found out that books with fewer pages are more popular than the ones with more pages. 
            So we recommend you to read a book with a rating of **7.5-8.0** and pages ranging between **160 -300**.''')
            dx = df.sort_values(by=('min_max'), ascending=False)[0:100]
            fig = px.scatter(dx, x=dx["min_max"].values, y=dx["num_ratings"], hover_name=dx["title"], size=dx['num_pages']*10000,
                            hover_data=['num_pages', 'author'], labels={
                "x": "Average Ratings",
                "y": "Number of Ratings",

            }, color=dx["author"])

            # fig.update_traces(marker=dict(size=df['num_pages']/15))
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            fig.update(layout_showlegend=False)
            fig.update_layout(plot_bgcolor="black", height=1000, width=1400,
                            title_text='Number of Ratings in comparison to the Number of Ratings, in relation to Pages')
            st.plotly_chart(fig)

        # Another 1
        with st.beta_expander("• You read a book based on it's Genre? We got that covered"):
            st.subheader('The Genres:')
            st.markdown('''Here we created the diagram describing the top 10 of most popular genres.
            The leading Fiction genre with 685 books is really worth checking out. 
            If you are keen on reading Classical books, we are happy to tell you that 375 books on our list are available to read.''')
            dfclean = df.dropna()

            df_dummy = pd.DataFrame(dfclean.genres.str.split(',', 1).tolist(),
                                    columns=['g1', 'g2'])
            df_dummy = df_dummy.dropna()

            df2 = pd.DataFrame(df_dummy.g2.str.split(',', 1).tolist(),
                            columns=['g2', 'g3'])
            df2 = df2.dropna()
            t = []
            for i in df_dummy.g1:
                t.append((i.strip('[').strip(',').strip("''")))

            r = []
            for i in df2.g2:
                r.append((i.strip('[').strip(',').strip("'").strip(" '")))

            s = []
            for i in df2.g3:
                s.append((i.strip(']').strip(',').strip("'").strip(" '")))
            from collections import Counter
            z = t + r + s
            dfsecond = pd.DataFrame({"Genre": Counter(z).keys(),
                                    "counts": Counter(z).values()})
            dfsecond = dfsecond[:10]
            fig = px.bar(dfsecond, x="Genre", y="counts", barmode="group", hover_name=dfsecond["Genre"], color="Genre", labels={
                "Genre": "Genre category",
                "counts": "Number of Books",

            })
            fig.update_layout(plot_bgcolor="black", height=400,
                            width=800, title_text='Genres')
            fig.update(layout_showlegend=False)
            for data in fig.data:
                data["width"] = 0.4
            st.plotly_chart(fig)
            
        with st.beta_expander('• Are you thinking about the Most Reviewed Authors?'):
            st.subheader('The authors:')
            st.markdown('''We know how much the number of reviews about any product influences our decision on actually investing in it.
            We present you an easy way of deciphering which Author's work has been reviewed the most. This way you can be sure that your precious
            time will be rewarded! ''')
            r_books = df.groupby(['author', 'title','min_max'])['num_reviews'].quantile(0.9)
            r_books = pd.DataFrame(r_books).sort_values(
                by=['num_reviews'], ascending=False)[0:50]
            r_books = r_books.reset_index()

            fig = px.bar(r_books, x="author", y="num_reviews", hover_name="title",
                         hover_data=['min_max','author'],
                        labels={
                            "x": "Author",
                            "y": "Number of reviews",

                        }, color="author")

            # fig.update_traces(marker=dict(size=df['num_pages']/15))
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            fig.update(layout_showlegend=False)
            fig.update_layout(plot_bgcolor="black", height=500,
                            title_text='Top 50 Most Reviewed books')
            st.plotly_chart(fig)


app()
