import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from itertools import cycle
from st_clickable_images import clickable_images


##################################################################################################################################
########### Preparation :

# Configurer la mise en page de la page Streamlit
st.set_page_config(layout="wide")

df = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/DF_COS_FINAL.csv')
###### creation df statik par genre 
df_statik = df
# explode des genres
df_statik['genres'] = df_statik['genres'].str.split(',')  # Convertir les chaînes de caractères en listes
df_statik = df_statik.explode('genres')
# on garde le premier genre de chaque films
df_statik = df_statik.groupby('tconst').agg({
    'personne': lambda x: ', '.join(x.astype(str)),
    'job': lambda x: ', '.join(x.astype(str)),
    'titre' : 'first',
    'Title' : 'first',
    'isAdult' : 'first',
    'imdbVotes' : 'first',
    'Runtime' : 'first',
    'Awards' : 'first',
    'Poster' : 'first',
    'annee': 'first',
    'genres': 'first',
    'note': 'first',
    'Plot': 'first',
    }).reset_index()
# on tri par note et filtre le nb de vote
df_statik= df_statik.sort_values(by='note', ascending=False)
df_statik = df_statik[df_statik['imdbVotes'] > 100000]

# on vire l'indien de la ville :) 
df_statik = df_statik.drop(df_statik[df_statik['titre'] == 'Jai Bhim'].index)
df_statik = df_statik.drop(df_statik[df_statik['titre'] == 'The Kashmir Files'].index)
df_statik = df_statik.drop(df_statik[df_statik['titre'] == 'Dil Bechara'].index)

# on va ensuite faire des df par genres pour laffichage statik
Action = df_statik[df_statik['genres'] == 'Action'].head(6)
Crime = df_statik[df_statik['genres'] == 'Crime'].head(6)
Drama = df_statik[df_statik['genres'] == 'Drama'].head(6)
Comedy = df_statik[df_statik['genres'] == 'Comedy'].head(6)
Animation = df_statik[df_statik['genres'] == 'Animation'].head(6)
Mystery = df_statik[df_statik['genres'] == 'Mystery'].head(6)
Horror = df_statik[df_statik['genres'] == 'Horror'].head(6)



list_Action = Action['titre'].to_list()
list_Crime = Crime['titre'].to_list()
list_Drama = Drama['titre'].to_list()
list_Comedy = Comedy['titre'].to_list()
list_Animation = Animation['titre'].to_list()
list_Mystery = Mystery['titre'].to_list()
list_Horror = Horror['titre'].to_list()


####### preparation mise en page

# Définir le style CSS pour la ligne de séparateur
separator_style = """ margin-top: 1rem; margin-bottom: 1rem; border-top: 2px solid #ddd;"""

# Import police
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');</style>", unsafe_allow_html=True)



##################################################################################################################################
########### Debut de la page :


############################# Action #############################

# Titre
st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TOP ACTION :</p>', unsafe_allow_html=True)
#Display les affiches clickable

clicked = clickable_images(
    [df[df.titre == titre]["Poster"].values[0] for titre in list_Action],
    titles=[titre for titre in list_Action],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "8px", "height": "400px"})

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

############################# Crime #############################

# Titre
st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TOP CRIME :</p>', unsafe_allow_html=True)
#Display les affiches clickable

clicked = clickable_images(
    [df[df.titre == titre]["Poster"].values[0] for titre in list_Crime],
    titles=[titre for titre in list_Crime],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "8px", "height": "400px"})

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

############################# Drama #############################

# Titre
st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 32px; ">&nbsp;&nbsp;&nbsp;&nbsp; TOP DRAMA :</p>', unsafe_allow_html=True)
#Display les affiches clickable

clicked = clickable_images(
    [df[df.titre == titre]["Poster"].values[0] for titre in list_Drama],
    titles=[titre for titre in list_Drama],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "8px", "height": "400px"})

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

############################# Comedy #############################

# Titre
st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp; TOP COMEDY :</p>', unsafe_allow_html=True)
#Display les affiches clickable

clicked = clickable_images(
    [df[df.titre == titre]["Poster"].values[0] for titre in list_Comedy],
    titles=[titre for titre in list_Comedy],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "8px", "height": "400px"})

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

############################# Animation #############################

# Titre
st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 32px; ">&nbsp;&nbsp;&nbsp; TOP ANIMATION :</p>', unsafe_allow_html=True)
#Display les affiches clickable

clicked = clickable_images(
    [df[df.titre == titre]["Poster"].values[0] for titre in list_Animation],
    titles=[titre for titre in list_Animation],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "8px", "height": "400px"})

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

############################# Mystery #############################

# Titre
st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TOP MYSTERY :</p>', unsafe_allow_html=True)
#Display les affiches clickable

clicked = clickable_images(
    [df[df.titre == titre]["Poster"].values[0] for titre in list_Mystery],
    titles=[titre for titre in list_Mystery],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "8px", "height": "400px"})

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

############################# Horror #############################

# Titre
st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TOP HORROR :</p>', unsafe_allow_html=True)
#Display les affiches clickable

clicked = clickable_images(
    [df[df.titre == titre]["Poster"].values[0] for titre in list_Horror],
    titles=[titre for titre in list_Horror],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "8px", "height": "400px"})

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)















