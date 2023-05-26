import streamlit as st
import pandas as pd
from PIL import Image

##################################################################################################################################
########### Preparation :

# Configurer la mise en page de la page Streamlit
st.set_page_config(layout="wide")

##### images 
logo = Image.open('images/Pixel_prod.png')
Chrys = Image.open('images/chrys.png')
Lucas = Image.open('images/lucas.jpg')
Antho = Image.open('images/antho.jpg')
imdb = Image.open('images/imdb.png')
python = Image.open('images/python.png')
pandas = Image.open('images/pandas.svg')
plot = Image.open('images/plotly.png')
knn = Image.open('images/knn.png')
stream = Image.open('images/stream.png')
bdd = Image.open('images/bdd.png')
tabl = Image.open('images/table.png')

##### polices

# Import police
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');</style>", unsafe_allow_html=True)
# creation variable police
font = "Roboto Condensed"

##### couleurs

# MEMO couleurs

# color_text_1 = color: #4F4F4F 
# color_sep =  color: 

##### separateurs

# Définir le style CSS pour la ligne de séparateur
separator_style = """ margin-top: 1rem; margin-bottom: 1rem; border-top: 2px solid #ddd;"""

##################################################################################################################################
########### Debut de la page :

##### Header

logo_container = st.container()

gauche,logo_cont,droite = logo_container.columns([2, 6, 2])

# afficher le logo
with logo_cont:
    
    st.image(logo, use_column_width=True)
    
# Ajouter espaces
st.markdown("<br>", unsafe_allow_html=True)


# Creer des onglets
tab1, tab2 = st.tabs([ 'L\'EQUIPE','LE PROJET'])

# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)




###### section 1 : presentation de l'equipe

with tab1:
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 45px; text-align: center;">LES MEMBRES DE L\'EQUIPE</p>', unsafe_allow_html=True)

    # Ajouter espaces
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    

    #### Chrys ####

    membre_container1 = st.container()

    gauche,photo_container1, sep_container1, info_container1,droite = membre_container1.columns([2, 2, 1, 3, 2])

    with photo_container1:

        # image
        st.image(Chrys, width=250)

    with info_container1:

        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # Nom
        st.markdown('<p style="color: #4F4F4F; font-size: 35px; text-align: center;">Chrysanthe</p>', unsafe_allow_html=True)
        # Texte
        st.markdown('<p style="color: #333333; font-size: 20px; text-align: center; ">Realisations :</p>', unsafe_allow_html=True)
        # Texte
        st.markdown('<p style="color: #333333; font-size: 18px; text-align: center;">Traitement des donnees, Analyse, Realisation de Kpi, Machine Learning , Web-app</p>', unsafe_allow_html=True)


    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)

    #### Lucas ####

    membre_container2 = st.container()

    gauche2,info_container2, sep_container2, photo_container2, droite2 = membre_container2.columns([2, 3, 1, 2, 2])

    with info_container2:

        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # Nom
        st.markdown('<p style="color: #4F4F4F; font-size: 35px; text-align: center;">Lucas</p>', unsafe_allow_html=True)
        # Texte
        st.markdown('<p style="color: #333333; font-size: 20px; text-align: center; ">Realisations :</p>', unsafe_allow_html=True)
        # Texte
        st.markdown('<p style="color: #333333; font-size: 18px; text-align: center;">Traitement des donnees, Analyse, Realisation de Kpi, Machine Learning , Web-app</p>', unsafe_allow_html=True)



    with photo_container2:

        # image
        st.image(Lucas, width=250)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)

    #### Antho ####

    membre_container3 = st.container()

    gauche3, photo_container3, sep_container3, info_container3, droite3 = membre_container3.columns([2, 2, 1, 3, 2])

    with photo_container3:

        # image
        st.image(Antho, width=250)

    with info_container3:

        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # Nom
        st.markdown('<p style="color: #4F4F4F; font-size: 35px; text-align: center;">Anthony</p>', unsafe_allow_html=True)
        # Texte
        st.markdown('<p style="color: #333333; font-size: 20px; text-align: center; ">Realisations :</p>', unsafe_allow_html=True)
        # Texte
        st.markdown('<p style="color: #333333; font-size: 18px; text-align: center;">Traitement des donnees, Analyse, Realisation de Kpi, Machine Learning , Web-app</p>', unsafe_allow_html=True)
        
        # Ajouter espaces
        st.markdown("<br><br>", unsafe_allow_html=True)

        
   ##################### section 2 : projet  #####################

with tab2:
    
    projet_container = st.container()

    gauche,text_cont,droite = projet_container.columns([1, 8, 1])
    
    with text_cont:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)

        # Titre
        st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 45px; text-align: center;">LE PROJET</p>', unsafe_allow_html=True)

        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)

        # Texte
        st.markdown('<p style="color: #333333; font-size: 20px; text-align: center;">Le client a besoin en premier lieu d\'une analyse globale du marche cinematographique, que nous avons realise grace a la base de donnee fournit. Nous avons ensuite retranscrit notre analyse sous forme de graphique.</p>', unsafe_allow_html=True)

        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)

        # Texte
        st.markdown('<p style="color: #333333; font-size: 20px; text-align: center;">Dans un second temps vous vouliez mettre a disposition des utilisateurs, une plateforme de recommendation de film. Pour cette tache nous avons commencee par developper un algorithme de recommendation grace au machine learning, algorithme que nous avons ensuite integre dans une application web qui servira de support utilisateur. </p>', unsafe_allow_html=True)

         # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Ajouter séparateur 
    st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

###### les outils

    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 45px; text-align: center;">LES OUTILS UTILISES</p>', unsafe_allow_html=True)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
     #### Base de donnees & API ####

    outil_container1 = st.container()
    info_contain1, photo_contain1 = outil_container1.columns([5, 3])

    with info_contain1:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # texte
        st.markdown('<p style="color: #4F4F4F; font-size: 30px; text-align: center;">Base de donnees & API</p>', unsafe_allow_html=True)

    with photo_contain1:

        # image
        st.image(imdb, width=150)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)

      #### Traitement des donnees  ####

    outil_container2 = st.container()
    info_contain2, photo_contain2 = outil_container2.columns([5, 3])

    with info_contain2:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # texte
        st.markdown('<p style="color: #4F4F4F; font-size: 30px; text-align: center;">Traitement des donnees</p>', unsafe_allow_html=True)

    with photo_contain2:

        # image
        st.image(python, width=200)
        # image
        st.image(pandas, width=200)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    

    #### DataViz ####

    outil_container3 = st.container()
    info_contain3, photo_contain3 = outil_container3.columns([5, 3])

    with info_contain3:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # texte
        st.markdown('<p style="color: #4F4F4F; font-size: 30px; text-align: center;">DataViz</p>', unsafe_allow_html=True)

    with photo_contain3:

        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # image
        st.image(plot, width=200)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
    #### Machine Learning ####

    outil_container4 = st.container()
    info_contain4, photo_contain4 = outil_container4.columns([5, 3])

    with info_contain4:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # texte
        st.markdown('<p style="color: #4F4F4F; font-size: 30px; text-align: center;">Machine Learning</p>', unsafe_allow_html=True)

    with photo_contain4:

        # image
        st.image(knn, width=200)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
    #### Web-App ####

    outil_container5 = st.container()
    info_contain5, photo_contain5 = outil_container5.columns([5, 3])

    with info_contain5:
        # Ajouter espaces
        st.markdown("<br>", unsafe_allow_html=True)
        # texte
        st.markdown('<p style="color: #4F4F4F; font-size: 30px; text-align: center;">Web-App</p>', unsafe_allow_html=True)

    with photo_contain5:

        # image
        st.image(stream, width=200)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
       # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Ajouter séparateur 
    st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    
###### les Donnees

   
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald;font-size: 45px; text-align: center;">LES DONNEES</p>', unsafe_allow_html=True)

    
   
 # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    data_container = st.container()
    photo_cont, sepp, infoo_cont = data_container.columns([6, 1, 3])
    
    
    with photo_cont:
    
        # Ajouter espaces
        st.markdown("<br><br>", unsafe_allow_html=True)
        # image
        st.image(bdd, width=800)
        
    with infoo_cont:
        
        st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">Notre DF final :</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px;">Nous avons utilisé les tables de données IMDB pour notre analyse. Notre table principale est appelée "title.principals" et elle a été fusionnée avec d\'autres tables en utilisant les colonnes "tconst" et "nconst". Nous avons appliqué un filtre sur certaines colonnes pour sélectionner les données pertinentes. Les critères de filtrage étaient les suivants :</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px;">- La colonne "is_adulte" doit être égale à 0, ce qui signifie que le contenu est destiné à un public de tous âges.</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px;">- L\'année "start_year" doit être supérieure à 1980.</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px;">--> Ce choix d’année est expliqué par notre KPI sur le nb de votes IMBD</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px;">- Le "average_rating" doit être supérieur à 5.</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px;">- Les régions "region" et langues "language" doivent être  soit  française et anglophone</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px; ">Ensuite, nous avons effectué une fusion (merge) avec l\'API OMDb (Open Movie Database) afin de récupérer des informations supplémentaires pour chaque titre. Nous avons extrait les colonnes telles que "plot" (synopsis), "box_office" (recettes), "affiche" (affiche du film) et "awards" (récompenses).</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #333333; font-size: 18px;">Cette approche nous a permis de combiner les données IMDB avec celles de l\'API OMDb, afin d\'enrichir notre ensemble de données avec des informations détaillées sur les titres sélectionnés.</p>', unsafe_allow_html=True)

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Ajouter séparateur 
    st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)


    ############### recommendation

    # Titre
    st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 45px; text-align: center;">RECOMMANDATIONS</p>', unsafe_allow_html=True)


    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown('<p style="color: #333333; font-size: 18px;">1. Historique de visionnage : Analysez l\'historique de visionnage pour des recommandations personnalisées, Recommandez des films similaires ou explorez d\'autres dans le même univers cinématographique.</p>', unsafe_allow_html=True)

    st.markdown('<p style="color: #333333; font-size: 18px;">2. Recommandations basées sur les préférences des utilisateurs : Permettez aux utilisateurs de donner leur avis sur les films visionnés par un bouton aimé ou pas aimé, Identifiez les utilisateurs ayant des préférences similaires, Recommandez des films appréciés par ces utilisateurs similaires, Retirez de la recommandation les films ayant < d’une note fixée.</p>', unsafe_allow_html=True)

    st.markdown('<p style="color: #333333; font-size: 18px;">3. Propositions de films par franchise : Ajoutez des sections dédiées aux franchises populaires.5Disney, Pixar, MCU, Les sagas : Harry Potter, Hunger Games, Twilight... , Facilitez la découverte de films liés à ces franchises spécifiques.</p>', unsafe_allow_html=True)

    st.markdown('<p style="color: #333333; font-size: 18px;">4. Recommandations basées sur les tendances actuelles : Utilisez les données en temps réel pour identifier les films populaires, Proposer les films les plus discutés et les tendances émergentes.</p>', unsafe_allow_html=True)

    st.markdown('<p style="color: #333333; font-size: 18px;">5. Recommandations basées sur les thèmes et les motifs : Identifiez les thèmes récurrents dans les films, EX : Films de voyage dans le temps, d’époque, d’espionnage, de vengeance (recherche mot clé dans les synopsis..), Recommandez des films partageant des thèmes similaires.</p>', unsafe_allow_html=True)

    st.markdown('<p style="color: #333333; font-size: 18px;">6. Recommandations similaires pour les séries : Appliquez les mêmes principes de recommandation pour les séries télévisées.</p>', unsafe_allow_html=True)


    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)


    tar_container4 = st.container()
    gauche,tarif,droite = tar_container4.columns([2, 6, 2])

    # afficher le tableau
    with tarif:

        st.image(tabl, use_column_width=True)

    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
