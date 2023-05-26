import streamlit as st
import pandas as pd
import base64
import numpy as np
import webbrowser
from itertools import cycle
from st_clickable_images import clickable_images
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from PIL import Image
from imdb import Cinemagoer


#Suppréssion des bordures droite et gauches
st.set_page_config(layout="wide")

#Call api de l'URL
ia = Cinemagoer()

#Suppréssion des bordures Haute
page_Top = f"""<style>
.appview-container .main .block-container{{
max-width: 100%;
padding-top: {0.5}rem;
padding-right: {1}rem;
padding-left: {1}rem;
padding-bottom: {1}rem}}
</style>"""

st.markdown(page_Top, unsafe_allow_html=True)

#Création d'une session state our jonction selection et classement
if 'myList' not in st.session_state: 
        st.session_state['myList'] = []

clicked_list = st.session_state['myList']

#Création d'une session state our jonction rechercher et watchlist
if 'My_watchList' not in st.session_state: 
        st.session_state['My_watchList'] = []

clicked_watchlist = st.session_state['My_watchList']


#Import du DF
df = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/DF_COS_FINAL.csv', sep =",")

#Prépare la matice pour les furtures recommendation !!!!!CODE A EXECUTER UNE SEUL FOIS PAR PAGE!!!!!
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])


####### creation liste pour reco statik par genre 

list_Action = ['The Dark Knight : Le Chevalier noir', 'Le Seigneur des anneaux : Le Retour du roi', 'Inception', "Le Seigneur des anneaux : La Communauté de l'anneau", 'Le Seigneur des anneaux : Les Deux Tours', 'Matrix']
list_Crime = ['Pulp Fiction', 'Le Silence des agneaux', 'La ligne verte', 'La cité de Dieu', 'Seven', 'Les infiltrés']
list_Drama = ['Les Évadés', 'Fight Club', 'Forrest Gump', 'Il faut sauver le soldat Ryan', 'Le Cinema Paradis', 'Whiplash']
list_Comedy = ['La vie est belle', '3 Idiots', "Le fabuleux destin d'Amélie Poulain", 'The Truman Show', 'Snatch - Tu braques ou tu raques', 'Un jour sans fin']
list_Animation = ['Le tombeau des lucioles', 'Your Name.', 'Mon voisin Totoro', 'Mary et Max.', 'La Belle et la Bête', "L'étrange Noël de monsieur Jack"]
list_Mystery = ['Memento', 'Shutter Island', "L'Armée des 12 singes", 'Lost Highway', 'Identity', 'La neuvième porte']
list_Horror = ['The Thing', 'Get Out', 'Les autres', 'Saw', 'Conjuring: Les dossiers Warren', 'Scream']

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

#"https://image.noelshack.com/fichiers/2023/21/4/1685009023-wildflix-patern.jpg",
#Bouton de la barre de menu

selection = clickable_images(
    ["https://image.noelshack.com/fichiers/2023/21/4/1685008386-selection-patern.jpg","https://image.noelshack.com/fichiers/2023/21/4/1685009007-classement-patern.jpg","https://image.noelshack.com/fichiers/2023/21/4/1685008694-recherche-patern.jpg","https://image.noelshack.com/fichiers/2023/21/4/1685009017-watchlist-patern.jpg","https://image.noelshack.com/fichiers/2023/21/4/1685026780-watchlist-patern-2.jpg"],
    titles=["Selection"],
    div_style={"display": "flex", "justify-content": "center",},
    img_style={"margin": "", "height": "55px"},)

#------------------------------------------WILDFLIX------------------------------------------------

if selection == 4 or selection == -1  :
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
    # Ajout espace entre picto et affiche
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<p style="color: #6495ED; font-family:Oswald; font-size: 32px; text-align: center;"> VEUILLEZ SELECTIONER 3 FILMS</p>', unsafe_allow_html=True)
    
    # Ajout espace entre picto et affiche
    st.markdown("<br>", unsafe_allow_html=True)

    #Liste des titres pour affichage a clicker
    list_affiche = ["Avatar","Avengers","Pulp Fiction","Les Évadés","Inception","Le Seigneur des anneaux : Le Retour du roi", "Fight Club", "Love Actually", "Interstellar", "Blade Runner", "Forrest Gump","The Dark Knight : Le Chevalier noir","Princesse Mononoké","The Truman Show","Le fabuleux destin d'Amélie Poulain","Matrix","Les Tuche","Gladiator","The Big Lebowski","Requiem for a Dream"] 


    #Display les affiches clickable

    clicked = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_affiche],
        titles=[i for i in list_affiche],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "490px"})


    
    #Session state pour stocker les films cliké 


    def click_movie(x):
        clicked_titre = list_affiche[clicked]
        clicked_list.append(clicked_titre)


    if len(st.session_state['myList']) < 3 :   
        if clicked > -1 :
            click_movie(clicked) 
        
 



#------------------------------------------CLASSEMENT------------------------------------------------
#Selection de page
if selection == 1:
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

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
                
            
            
    #Afficher les 6 films recommendé et clickable
    st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 25px;">&nbsp; D\'APRES VOTRE SELECTION :</p>', unsafe_allow_html=True)
    
    #Demande à l'utilisateur d'aller clicker dans selection
    if len(clicked_list) == 0 :
        st.markdown('<p style="color: #0000FF;font-family:Oswald; font-size: 25px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; VEUILLEZ SELECTIONNER 3 FILMS DANS L\'ONGLET SELECTION</p>', unsafe_allow_html=True)
        
        
    clicked_reco_selection = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_reco],
        titles=[i for i in list_reco],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "405px"})
    
    
    
    #Renvoi vers l'URL TRAILER
    if clicked_reco_selection > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_reco[clicked_reco_selection]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])
        
    
    
        

    ##################################################################################################################################
    ########### STATIC:


    ############################# Action #############################

     # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    # Titre
    st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 25px;">&nbsp; TOP ACTION :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked_reco_selection_2 = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Action],
        titles=[titre for titre in list_Action],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "411px"})
    
     #Renvoi vers l'URL TRAILER
    if clicked_reco_selection_2 > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_Action[clicked_reco_selection_2]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    ############################# Crime #############################

    # Titre
    st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 25px;">&nbsp; TOP CRIME :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked_reco_selection_3 = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Crime],
        titles=[titre for titre in list_Crime],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "411px"})
    
      #Renvoi vers l'URL TRAILER
    if clicked_reco_selection_3 > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_Crime[clicked_reco_selection_3]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    ############################# Drama #############################

    # Titre
    st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 25px; ">&nbsp; TOP DRAMA :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked_reco_selection_4 = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Drama],
        titles=[titre for titre in list_Drama],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "405px"})

    
      #Renvoi vers l'URL TRAILER
    if clicked_reco_selection_4 > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_Drama[clicked_reco_selection_4]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    ############################# Comedy #############################

    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 25px;">&nbsp; TOP COMEDY :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked_reco_selection_5 = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Comedy],
        titles=[titre for titre in list_Comedy],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "405px"})
    
          #Renvoi vers l'URL TRAILER
    if clicked_reco_selection_5 > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_Comedy[clicked_reco_selection_5]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    ############################# Animation #############################

    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald;font-size: 25px; ">&nbsp; TOP ANIMATION :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked_reco_selection_6 = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Animation],
        titles=[titre for titre in list_Animation],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "400px"})
    
         #Renvoi vers l'URL TRAILER
    if clicked_reco_selection_6 > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_Animation[clicked_reco_selection_6]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    ############################# Mystery #############################

    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 25px;">&nbsp; TOP MYSTERY :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked_reco_selection_7 = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Mystery],
        titles=[titre for titre in list_Mystery],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "405px"})
    
         #Renvoi vers l'URL TRAILER
    if clicked_reco_selection_7 > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_Mystery[clicked_reco_selection_7]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    ############################# Horror #############################

    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 25px;">&nbsp;&nbsp; TOP HORROR :</p>', unsafe_allow_html=True)
    #Display les affiches clickable

    clicked_reco_selection_8 = clickable_images(
        [df[df.titre == titre]["Poster"].values[0] for titre in list_Horror],
        titles=[titre for titre in list_Horror],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "4px", "height": "405px"})
    
           #Renvoi vers l'URL TRAILER
    if clicked_reco_selection_8 > -1 :
        #Converti l'indice clické en titre
        clicked_titre = list_Horror[clicked_reco_selection_8]
        #Converti le titre en tconst
        tconst = df[df.titre == clicked_titre]["tconst"].values[0]
        
       
        #Suppression du tt du tconst
        tconst = tconst[2:]

        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
        Id_movie = ia.get_movie(tconst)
        webbrowser.open_new_tab(Id_movie["videos"][0])

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
        

    
#------------------------------------------RECHERCHE------------------------------------------------

#Selection de page
if selection == 2:
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    #SWITCH ENTRE MOVIE  et Casting
    switch = clickable_images(
    ["https://image.noelshack.com/fichiers/2023/21/4/1685022195-switch-film.jpg","https://image.noelshack.com/fichiers/2023/21/4/1685022213-switch-casting.jpg"],
    titles=["Film","Casting"],
    div_style={"display": "flex", "justify-content": "left",},
    img_style={"margin": "", "height": "22px"},)
    
    
    
#+++++++++++++++++++++++++++++++++++++++++RECO FILM++++++++++++++++++++++++++++++++++++++++++++++   
    if switch == 0 or switch == -1 :
        
        # style separateur
        separator_style = """ height: 400px; border-left: 1px solid #ddd;"""
        container_style = """ display: flex; justify-content: center; align-items: center; height: 300px; """


        ################################################## select box  #############################################################

        # creation d'un container pour definir la taille de la selectbar
        selectbox_container = st.container()
        selecteur, vide = selectbox_container.columns([3 ,7])

        with selecteur:
            # Création de la liste des titres uniques
            titres = df['titre'].unique()
            # Changement du premier titre de la liste par premier titre selectioné pour apparition à l'ouverture
            if len(clicked_list) > 0 :
                titres = np.insert(titres,0,clicked_list[0])
            else :
                titres = np.insert(titres,0,"Avengers")
            # Création de la barre de recherche avec suggestions
            option = st.selectbox("",
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
         
        # creation dun container pour button
            button_container2 = st.container()
            seppppp2, button122, button2222 = button_container2.columns([1, 3, 6])
            
            with button122:
                 #Bouton Trailer
                Trailer = st.button("TRAILER")
                if Trailer :
                    #Converti le titre en tconst
                    tconst = df[df.titre == option]["tconst"].values[0]

                    #Suppression du tt du tconst
                    tconst = tconst[2:]

                    #Récupére les info du film a aprtir de l'ID = (tcons - tt)
                    Id_movie = ia.get_movie(tconst)
                    webbrowser.open_new_tab(Id_movie["videos"][0])

                    
            with button2222:
                #Bouton Watchlist
                Watchlist = st.button("WATCHLIST")
                if Watchlist :
                    clicked_watchlist.append(option)

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

        movie_user_likes = film_titre
        movie_index = get_index_from_title(movie_user_likes)

        knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
        knn_model.fit(count_matrix)
        _, indices = knn_model.kneighbors(count_matrix[movie_index], n_neighbors=15)


        for index in indices.flatten()[1:]:
            x = get_title_from_index(index)
            reco.append(x)

        #Display les affiches clickable

        clicked_search = clickable_images(
                [df[df.titre == titre]["Poster"].values[0] for titre in reco],
                titles=[i for i in reco],
                div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                img_style={"margin": "4px", "height": "350px"})


        # FILM RECOMMENDER CLICK
        if clicked_search > -1 :

            #Conversion de l'indice du click en titre 
            clicked_titre = reco[clicked_search]

            film_select_click = df[df['titre'] == clicked_titre]
            film_titre_click = film_select_click['titre'].values[0]
            film_image_click = film_select_click['Poster'].values[0]
            film_annee_click = film_select_click['annee'].values[0]
            film_resume_click = film_select_click['Plot'].values[0]
            film_casting_click = film_select_click['personne'].values[0]
            film_awards_click = film_select_click['Awards'].values[0]

            with image2:
                # Ajouter espaces
                st.markdown("<br>", unsafe_allow_html=True)
                # affichage de l'image
                st.image(film_image_click)
                
                button_container22 = st.container()
                sepppppppp2, button1222, button22222 = button_container22.columns([1, 3, 6])
                
                with button1222:
                     #Bouton Trailer
                    Trailer_2 = st.button("TRAILER ")
                    if Trailer_2 :
                        #Converti le titre en tconst
                        tconst = df[df.titre == clicked_titre]["tconst"].values[0]

                        #Call api de l'URL
                        ia = Cinemagoer()
                        #Suppression du tt du tconst
                        tconst = tconst[2:]

                        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
                        Id_movie = ia.get_movie(tconst)
                        webbrowser.open_new_tab(Id_movie["videos"][0])

                with button22222:
                    #Bouton Watchlist
                    Watchlist_2 = st.button("WATCHLIST ")
                    if Watchlist_2 :
                        clicked_watchlist.append(clicked_titre)

            with info_film2:
                # Ajouter espaces
                st.markdown("<br>", unsafe_allow_html=True)
                # affichage titre + (annee)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:28px;'>{film_titre_click} ({film_annee_click}) :</p>", unsafe_allow_html=True)
                # affichage resume
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Synopsis :</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:17px;'>{film_resume_click}</p>", unsafe_allow_html=True)
                # affichage casting
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Casting :</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_casting_click}</p>", unsafe_allow_html=True)
                # affichage casting
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Awards :</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_awards_click}</p>", unsafe_allow_html=True)
               
                
#+++++++++++++++++++++++++++++++++++++++++RECO CASTING++++++++++++++++++++++++++++++++++++++++++++++
          
    if switch == 1 :
             
        # Import police
        st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');</style>", unsafe_allow_html=True)

        # style separateur
        separator_style = """ height: 400px; border-left: 1px solid #ddd;"""
        container_style = """ display: flex; justify-content: center; align-items: center; height: 300px; """




        ################################################## select box  #############################################################

        # creation d'un container pour definir la taille de la selectbar
        selectbox_container = st.container()
        selecteur_actor, vide = selectbox_container.columns([3,7])


        with selecteur_actor:
            # Création de la liste des acteurs uniques
            df_casting = df
            df_casting['personne'] = df_casting['personne'].str.split(',')  # Convertir les chaînes de caractères en listes
            df_casting = df_casting.explode('personne')
            list_casting = df_casting['personne'].unique()
            # Changement du premier titre de la liste par premier titre selectioné pour apparition à l'ouverture
            list_casting = np.insert(list_casting,0,"Tom Holland")
            # Création de la barre de recherche avec suggestions
            actor = st.selectbox(
                "",
                list_casting)

        ################################################## affichage bandeau films choisit + click reco #############################################################

        # creation du df avec uniquement les films de la personne selectionne
        df_actor = df[df['personne'].apply(lambda x: any(actor in sublist for sublist in x))]
        df_actor = df_actor.sort_values('note', ascending=False)
        df_actor = df_actor.head(15)


        reco_actor = df_actor['titre'].to_list()
        reco_actor = reco_actor[1:15]

        # on recup le meilleur film de lacteur selectionner
        premier_film = df_actor.iloc[0]
        titre_premier = premier_film['titre']

        # on recupere l'images et les infos du film selectionner pour l'affichage

        film_select = df[df['titre'] == titre_premier]
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

            # creation dun container pour button
            button_container = st.container()
            seppppp, button1, button2 = button_container.columns([1, 3, 6])

            with button1:
                #Bouton Trailer
                Trailer = st.button("TRAILER")
                if Trailer :
                    #Converti le titre en tconst
                    tconst = df[df.titre == titre_premier]["tconst"].values[0]

                    #Suppression du tt du tconst
                    tconst = tconst[2:]

                    #Récupére les info du film a aprtir de l'ID = (tcons - tt)
                    Id_movie = ia.get_movie(tconst)
                    webbrowser.open_new_tab(Id_movie["videos"][0])


            with button2:
                #Bouton Watchlist
                Watchlist = st.button("WATCHLIST")
                if Watchlist :
                    clicked_watchlist.append(titre_premier)

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





         ################################################## affichage films recommendation ############################################################


        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)

        # titre
        st.markdown('<p style="color: #4F4F4F;font-family:Oswald; font-size: 25px;">FILMS QUI POURRAIENT VOUS PLAIRE :</p>', unsafe_allow_html=True)




        #Display les affiches clickable

        clicked_search = clickable_images(
                [df[df.titre == titre]["Poster"].values[0] for titre in reco_actor],
                titles=[i for i in reco_actor],
                div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                img_style={"margin": "4px", "height": "350px"})


        # FILM RECOMMENDER CLICK
        if clicked_search > -1 :

            #Conversion de l'indice du click en titre 
            clicked_titre = reco_actor[clicked_search]

            film_select_click = df[df['titre'] == clicked_titre]
            film_titre_click = film_select_click['titre'].values[0]
            film_image_click = film_select_click['Poster'].values[0]
            film_annee_click = film_select_click['annee'].values[0]
            film_resume_click = film_select_click['Plot'].values[0]
            film_casting_click = film_select_click['personne'].values[0]
            film_awards_click = film_select_click['Awards'].values[0]

            with image2:

                st.markdown("<br>", unsafe_allow_html=True)
                # affichage de l'image
                st.image(film_image_click)

                # creation dun container pour button
                button2_container = st.container()
                sep555555, button11, button22 = button2_container.columns([1, 3, 6])


                with button11:
                    #Bouton Trailer
                    Trailer_2 = st.button("TRAILER ")
                    if Trailer_2 :
                        #Converti le titre en tconst
                        tconst = df[df.titre == clicked_titre]["tconst"].values[0]

                        #Suppression du tt du tconst
                        tconst = tconst[2:]

                        #Récupére les info du film a aprtir de l'ID = (tcons - tt)
                        Id_movie = ia.get_movie(tconst)
                        webbrowser.open_new_tab(Id_movie["videos"][0])

                with button22:
                    #Bouton Watchlist
                    Watchlist_2 = st.button("WATCHLIST ")
                    if Watchlist_2 :
                        clicked_watchlist.append(clicked_titre)

            with info_film2:
                # Ajouter espaces
                st.markdown("<br>", unsafe_allow_html=True)
                # affichage titre + (annee)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:28px;'>{film_titre_click} ({film_annee_click}) :</p>", unsafe_allow_html=True)
                # affichage resume
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Synopsis :</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:17px;'>{film_resume_click}</p>", unsafe_allow_html=True)
                # affichage casting
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Casting :</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_casting_click}</p>", unsafe_allow_html=True)
                # affichage casting
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:22px;'>Awards :</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #4F4F4F; font-family:Oswald; font-size:16px;'>{film_awards_click}</p>", unsafe_allow_html=True)

        

    
#------------------------------------------WATCHLIST------------------------------------------------

if selection == 3 :
    if len(clicked_watchlist) == 0 :
        st.markdown('<p style="color: #0000FF;font-family:Oswald; font-size: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; VOTRE WATCHLIST EST VIDE VEUILLEZ SELECTIONNER DES FILMS DANS L\'ONGLET RECHERCHE</p>', unsafe_allow_html=True)
        
    
    if len(clicked_watchlist) > 0 :
        
        #demande le nom d'utilsateur
        user_name = st.text_input("Entrer un nom d'utilisateur pour afficher la WATCHLIST")
        if len(user_name) > 0:
            #Création du DF watchlist
            df_concat = df.head(0)
            for i in clicked_watchlist :
                df_watchlist = df.loc[df["titre"] == i]
                df_concat = pd.concat([df_concat,df_watchlist])
            #Netoyage du DF
            df_concat.drop(df_concat.index[0], inplace =True)
            df_concat.drop(columns ={'Unnamed: 0', 'tconst','job','Title','isAdult','Poster','genres','Plot','combined_features', 'index','imdbVotes'}, inplace =True)
            df_concat = df_concat[['titre','annee','note','personne','Runtime','Awards']]

            #Création du bouton de téléchargment   
            def convert_df_to_csv(df):
              # IMPORTANT: Cache the conversion to prevent computation on every rerun
              return df.to_csv().encode('utf-8')

            st.download_button(
              label="DOWNLOAD WATCHLIST",
              data=convert_df_to_csv(df_concat),
              file_name='Watchlist.csv',
              mime='text/csv',
        )      


            #Afficher la watchlist
            # Ajouter espaces
            st.markdown("<br><br>", unsafe_allow_html=True)

            # creation d'un container pour bandeau affichage film selectionner + film recommendation cliquer
            affichage_container = st.container()
            image, info_film,  = st.columns([2,8])

            for i in clicked_watchlist :
                film_select = df[df['titre'] == i]
                film_titre = film_select['titre'].values[0]
                film_image = film_select['Poster'].values[0]
                film_annee = film_select['annee'].values[0]
                film_resume = film_select['Plot'].values[0]
                film_casting = film_select['personne'].values[0]
                film_awards = film_select['Awards'].values[0]


                st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

                # FILM SELECTIONNER
                with image:
                    # Ajouter espaces
                    #st.markdown("<br>", unsafe_allow_html=True)
                    # affichage de l'image
                    st.image(film_image)

                with info_film:
                    # Ajouter espaces
                    #st.markdown("<br>", unsafe_allow_html=True)
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
                    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
                    

            
        

