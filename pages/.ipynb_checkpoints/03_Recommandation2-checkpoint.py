import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from itertools import cycle
from st_clickable_images import clickable_images


# Configurer la mise en page de la page Streamlit
st.set_page_config(layout="wide")

df = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/DF_COS_FINAL.csv')

# Import police
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');</style>", unsafe_allow_html=True)

# style separateur
separator_style = """ height: 400px; border-left: 1px solid #ddd;"""
container_style = """ display: flex; justify-content: center; align-items: center; height: 300px; """




################################################## select box  #############################################################

# creation d'un container pour definir la taille de la selectbar
selectbox_container = st.container()
selecteur_actor, vide = selectbox_container.columns([2,8])


with selecteur_actor:
    # Création de la liste des acteurs uniques
    df_casting = df
    df_casting['personne'] = df_casting['personne'].str.split(',')  # Convertir les chaînes de caractères en listes
    df_casting = df_casting.explode('personne')
    list_casting = df_casting['personne'].unique()
    # Changement du premier titre de la liste par premier titre selectioné pour apparition à l'ouverture
    list_casting = np.insert(list_casting,0,"Keanu Reeves")
    # Création de la barre de recherche avec suggestions
    actor = st.selectbox(
        "CASTING",
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
    sep555, button1, button2 = button_container.columns([1, 3, 6])

    with button1:
        #Bouton Trailer
        Trailer = st.button("TRAILER")
        if Trailer :
            #Converti le titre en tconst
            tconst = df[df.titre == option]["tconst"].values[0]

            #Call api de l'URL
            ia = Cinemagoer()
            #Suppression du tt du tconst
            tconst = tconst[2:]

            #Récupére les info du film a aprtir de l'ID = (tcons - tt)
            Id_movie = ia.get_movie(tconst)
            webbrowser.open_new_tab(Id_movie["videos"][0])


    with button2:
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

                #Call api de l'URL
                ia = Cinemagoer()
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








        


    
