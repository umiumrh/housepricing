import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import webbrowser


st.set_page_config(page_title="MCU project",
                   page_icon=":sparkles:",
                   layout="wide")

st.title('Welcome to my awesome data science project!')


#----DATA----
marvel = pd.read_csv('marvelmovies.csv')


#----PAGES----
def choice(page):
    if page == 'About This App':
        st.header('The Marvel Cinematic Universe! :sparkles:')
        st.write('This web app is exploring the Marvel Cinematic Universe films! This web app I created is based on my interest and I would love to share it to the public. Everyone knows about the MCU films, right? I mean, who does not?! But why has Marvel been so successful in recent years?')
        st.write('There are so many reasons to love Marvel movies. With such a diverse cast and range of films, there is something for everyone. The favorite movies for countries around the world range from Iron Man, Captain America, all the way to Spider-Man. And recently, I have watched the all new character in the MCU, the Morbius. Lucky me, the second movie of Doctor Strange is coming this May! It is no wonder that a person has its own favourite movie when there is so much to love about Marvel.')
        
    elif page == 'About Me':
        st.header('Hello, I am Umi, a fresh grad from Mathematics background. This is my first web application that I created! Have fun using it :revolving_hearts: \n Best, Umi.')
          
    elif page == 'The Films':
        option = st.selectbox(
            'Please select a title, be it a movie or a series from the MCU!',
            marvel['Title'].unique())
        
        movie_selection = marvel.query("Title == @option")
        
        title = movie_selection["Title"].iloc[0]
        imdb = movie_selection["IMDB Rating"].iloc[0]
        star = ":star:" * int(movie_selection["IMDB Rating"].iloc[0])
        year = movie_selection["Year Released"].iloc[0]
        
        st.header(f"{title}")
        st.header(f"Year {year}")
        st.subheader(f"{imdb} {star}")
        
        st.header("Synopsis")
        synopsis = movie_selection["Synopsis"].iloc[0]
        st.write(synopsis)
        
        st.header("Critics")
        critics = movie_selection["Critics Consensus"].iloc[0]
        st.write(critics)
    
    else:
        feature = st.selectbox('What do you want to see?',
                               ('Box Office ($ Million)',
                                'IMDB Rating',
                                'Chronological order')
                              )
        
        #movie_op = st.multiselect('Which movie would you like to compare together?', marvel["Title"].unique())
        
        if feature == 'Box Office ($ Million)':
            #st.bar_chart(marvel['Box Office ($ Million)'])
            fig = px.bar(marvel, x="Title", y="Box Office ($ Million)")
            fig.update_layout(height=600, width=1450)
            st.write(fig)
            
        elif feature == 'IMDB Rating':
        
            #st.bar_chart(marvel['IMDB Rating'])
            fig = px.bar(marvel, x="Title", y="IMDB Rating")
            fig.update_layout(height=600, width=1450)
            st.write(fig)
            
        else:
            i=0
            while i < 33:
                title = marvel["Title"].iloc[i]
                st.subheader(f"#{i+1} {title}")
                i+=1
            return
        return
            
    
    
    return



#----SIDE BAR----
st.sidebar.header("More on this App! :speech_balloon:")

page = st.sidebar.selectbox(
    'Pages',
    ('About This App','About Me','The Films','Features')
)
choice(page)

st.sidebar.header("Click for more discoveries!:point_down:")

if st.sidebar.button("Let's go"):
    url = 'https://www.marvel.com/movies'
    webbrowser.open_new_tab(url)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

