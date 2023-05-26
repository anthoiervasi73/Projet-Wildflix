import streamlit as st
import pandas as pd
import base64
from itertools import cycle
from st_clickable_images import clickable_images
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from PIL import Image

#Suppréssion des bordures droite et gauches
st.set_page_config(layout="wide")

#Suppréssion des bordures Haute
page_Top = f"""<style>
.appview-container .main .block-container{{
max-width: 100%;
padding-top: {0.5}rem;
padding-right: {1}rem;
padding-left: {1}rem;
padding-bottom: {1}rem}}
</style>"""

# style separateur
separator_style = """ height: 400px; border-left: 1px solid #ddd;"""
container_style = """ display: flex; justify-content: center; align-items: center; height: 300px; """
st.markdown(page_Top, unsafe_allow_html=True)


#Création d'une session state our jonction selection et classement
if 'myList' not in st.session_state: 
        st.session_state['myList'] = []

clicked_list = st.session_state['myList']


#Import du DF
df = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/DF_COS_FINAL.csv', sep =",")

#Prépare la matice pour les furtures recommendation !!!!!CODE A EXECUTER UNE SEUL FOIS PAR PAGE!!!!!
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])


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





#Supprime le header blanc en partie suppérieur
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url(https://image.noelshack.com/fichiers/2023/21/3/1684934164-degrade-fin.png);
background-size: 0%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


#Bouton de la barre de menu

selection = clickable_images(
    ["https://image.noelshack.com/fichiers/2023/21/3/1684946114-selection-gris-lm.jpg","https://image.noelshack.com/fichiers/2023/21/3/1684946439-classement-gris-lm.jpg","https://image.noelshack.com/fichiers/2023/21/3/1684946481-recherche-gris-lm.jpg","https://image.noelshack.com/fichiers/2023/21/3/1684946523-wild-flix-gris-lm.jpg"],
    titles=["Selection"],
    div_style={"display": "flex", "justify-content": "center",},
    img_style={"margin": "", "height": "57px"},)

#------------------------------------------WILDFLIX------------------------------------------------
if selection == 3 or selection == -1  :
    video_path = 'images\WILDFLIX.mp4'
    video_file = open(video_path, 'rb')
    video_bytes = video_file.read()
    base64_video = base64.b64encode(video_bytes).decode()
    
       # Define the CSS style to set the video width to 100%
    video_style = f"width: 100%; max-width: 100%;"

    # Display the video using the HTML video tag with the specified style
    st.markdown(
        f'<video autoplay loop muted style="{video_style}"><source type="video/mp4" src="data:video/mp4;base64,{base64_video}"></video>',
        unsafe_allow_html=True)



#------------------------------------------SELECTION------------------------------------------------


if selection == 0:
    # Ajout espace entre picto et affiche
    st.markdown("<br>", unsafe_allow_html=True)

    #Liste des titres pour affichage a clicker
    list_affiche = ["Avatar","Avengers","Pulp Fiction","Les Évadés","Inception","Le Seigneur des anneaux : Le Retour du roi", "Fight Club", "Love Actually", "Interstellar", "Blade Runner", "Forrest Gump","The Dark Knight : Le Chevalier noir","Princesse Mononoké","The Truman Show","Le fabuleux destin d'Amélie Poulain","Matrix","Les Tuche","Gladiator","The Big Lebowski","Requiem for a Dream"] 


    #Display les affiches clickable

    clicked = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_affiche],
        titles=[i for i in list_affiche],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "450px"})


    
    #Session state pour stocker les films cliké 


    def click_movie(x):
        clicked_titre = list_affiche[clicked]
        clicked_list.append(clicked_titre)


    if len(st.session_state['myList']) < 3 :   
        if clicked > -1 :
            click_movie(clicked) 
        
 



#------------------------------------------CLASSEMENT------------------------------------------------

if selection == 1:

    ############################# Selection #############################
    
    
    #Récupére le titre depuis l'index ( Pour algo reco)
    def get_title_from_index(index):
        return df[df.index == index]["titre"].values[0]

    #Récupére l'index depuis le titre
    def get_index_from_title(titre):
        return df[df.titre == titre]["index"].values[0]
    
    #Liste vide pour reco
    list_reco =[]
    
    # Limite a 3 film la selection et lance la def de recommendation
        
    if len(clicked_list) == 3 : 

        for click_movie in clicked_list :

            movie_user_likes = click_movie
            movie_index = get_index_from_title(movie_user_likes)

            knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
            knn_model.fit(count_matrix)
            _, indices = knn_model.kneighbors(count_matrix[movie_index], n_neighbors=3)


            for index in indices.flatten()[1:]:
                x = get_title_from_index(index)
                list_reco.append(x)
                
     # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
            
    #Afficher les 6 films recommendé et clickable
    st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; D\'APRES VOTRE SELECTION :</p>', unsafe_allow_html=True)
    clicked_reco = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_reco],
        titles=[i for i in list_reco],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "350px"})
    
    if len(clicked_list) == 0 :
        st.markdown('<p style="color: #FF0000;font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; VEUILLEZ SELECTIONER 3 FILMS DANS L\'ONGLET SELECTION</p>', unsafe_allow_html=True)



    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)


    ############################# Action #############################

    # Titre
    st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TOP ACTION :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Action],
        titles=[titre for titre in list_Action],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "350px"})

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
        img_style={"margin": "4px", "height": "350px"})

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
        img_style={"margin": "4px", "height": "350px"})

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
        img_style={"margin": "4px", "height": "350px"})

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
        img_style={"margin": "4px", "height": "350px"})

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
        img_style={"margin": "4px", "height": "350px"})

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
        img_style={"margin": "4px", "height": "350px"})

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)

    
#------------------------------------------RECO par RECHERCHE------------------------------------------------


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

if selection == 2:
    
    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
      
    
    ################################################## select box  #############################################################

    # creation d'un container pour definir la taille de la selectbar
    selectbox_container = st.container()
    selecteur, vide = selectbox_container.columns([2 ,8])

    with selecteur:
        # Création de la liste des titres uniques
        titres = df['titre'].unique()
        # Création de la barre de recherche avec suggestions
        option = st.selectbox(
            'RECHERCHE :',
            titres)

    ################################################## affichage bandeau films choisit + click reco #############################################################

    # on recupere l'images et les infos du film selectionner pour l'affichage

    film_select = df[df['titre'] == option]
    film_titre = film_select['titre'].values[0]
    film_image = film_select['Poster'].values[0]
    film_annee = film_select['annee'].values[0]
    film_resume = film_select['Plot'].values[0]
    film_casting = film_select['personne'].values[0]
    film_awards = film_select['Awards'].values[0]

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)

    # creation d'un container pour bandeau affichage film selectionner + film recommendation cliquer
    affichage_container = st.container()
    image, info_film, sep, image2, info_film2 = selectbox_container.columns([2, 2, 1, 2, 2])


    # FILM SELECTIONNER
    with image:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # affichage de l'image
        st.image(film_image)

    with info_film:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # affichage titre + (annee)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:28px;'>{film_titre} ({film_annee}) :</p>", unsafe_allow_html=True)
        # affichage resume
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Synopsis :</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:17px;'>{film_resume}</p>", unsafe_allow_html=True)
        # affichage casting
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Casting :</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_casting}</p>", unsafe_allow_html=True)
        # affichage casting
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Awards :</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_awards}</p>", unsafe_allow_html=True)

    # SEPARATEUR
    with sep:
        # Ajouter espaces
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        # affichage separateur
        st.markdown('<div style="{}"><div style="{}"></div></div>'.format(container_style, separator_style), unsafe_allow_html=True)


    # FILM RECOMMENDER CLICK

    with image2:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # affichage de l'image
        st.image(film_image)

    with info_film2:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # affichage titre + (annee)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:28px;'>{film_titre} ({film_annee}) :</p>", unsafe_allow_html=True)
        # affichage resume
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Synopsis :</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:17px;'>{film_resume}</p>", unsafe_allow_html=True)
        # affichage casting
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Casting :</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_casting}</p>", unsafe_allow_html=True)
        # affichage casting
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Awards :</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_awards}</p>", unsafe_allow_html=True)



     ################################################## affichage films recommendation ############################################################


    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # titre
    st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 25px;">FILMS QUI POURRAIENT VOUS PLAIRE :</p>', unsafe_allow_html=True)

    #Récupére le titre depuis l'index ( Pour algo reco)
    def get_title_from_index(index):
        return df[df.index == index]["titre"].values[0]

    #Récupére l'index depuis le titre
    def get_index_from_title(titre):
        return df[df.titre == titre]["index"].values[0]

    reco = []

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    movie_user_likes = film_titre
    movie_index = get_index_from_title(movie_user_likes)

    knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
    knn_model.fit(count_matrix)
    _, indices = knn_model.kneighbors(count_matrix[movie_index], n_neighbors=15)


    for index in indices.flatten()[1:]:
        x = get_title_from_index(index)
        reco.append(x)

    #Display les affiches clickable

    clicked = clickable_images(
            [df[df.titre == titre]["Poster"].values[0] for titre in reco],
            titles=[i for i in reco],
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
            img_style={"margin": "4px", "height": "350px"})
