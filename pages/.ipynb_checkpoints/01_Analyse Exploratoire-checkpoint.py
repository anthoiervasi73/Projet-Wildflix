import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio


##################################################################################################################################
########### Preparation :
# Configurer la mise en page de la page Streamlit
st.set_page_config(layout="wide")


# import data kpi Antho
kpi_top_ratings = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_director_ratings.csv')
kpi_top_nbfilm = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_director_nbfilm.csv')
# import data kpi Lucas
df_NUM_RATING = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_rating_date.csv')
df_RELEASE = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_serie_movie.csv')
df_ALL_TYPE = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_rating_all_category.csv')
# import data kpi Chrysanthe
df = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_kpy_chrys.csv')
top_titleTypes = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_top_titleTypes.csv')
df_base = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_base.csv')
df_HE = pd.read_csv('https://raw.githubusercontent.com/anthoiervasi73/Projet-Wildflix/master/df/df_HE.csv') 


##### polices

st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');</style>", unsafe_allow_html=True)

##### separateurs

# Définir le style CSS pour la ligne de séparateur
separator_style = """ margin-top: 1rem; margin-bottom: 1rem; border-top: 2px solid #ddd;"""


##################################################################################################################################
########### Debut de la page :

# Titre
st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 45px; text-align: center;">ANALYSE EXPLORATOIRE</p>', unsafe_allow_html=True)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


############ kpi 1 ############ 

# kpi 1 Lucas 
# code dataframe
df_NUM_RATING = df_NUM_RATING[df_NUM_RATING["startYear"] <= 2023]
df_NUM_RATING["numVotes"].fillna(0, inplace = True)
df_NUM_RATING["numVotes"] = df_NUM_RATING["numVotes"].astype(int)
df_NUM_RATING["startYear"] = pd.to_datetime(df_NUM_RATING["startYear"], format = "%Y")
df_NUM_RATING["Annees"] = df_NUM_RATING["startYear"].apply(lambda x: x.year//10*10)
df_pivot_NUM_RATING = df_NUM_RATING.pivot_table(index = "Annees", values = "numVotes", aggfunc = "sum")
# code kpi
fig_NUM_RATING = px.line(df_pivot_NUM_RATING, x = df_pivot_NUM_RATING.index, y = "numVotes", title = "Nombre de vote par decennie", 
               labels = {"numVotes" : " Voters", "Annees" : ""},markers=True, text = "numVotes",width=1400, height=550)
              
fig_NUM_RATING.update_layout(
    plot_bgcolor='white'
)
fig_NUM_RATING.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=False,
    linecolor='blue',
    gridcolor='lightgrey'
)
fig_NUM_RATING.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=False,
    linecolor='white',
    gridcolor='lightgrey'
)    
fig_NUM_RATING.update_traces(line_color="#A267AC", line_width=2, textposition="top left", textfont_color="black")
fig_NUM_RATING.add_vrect(x0= 1885, x1 = 1980, fillcolor ="red", opacity=0.1)
fig_NUM_RATING.add_vrect(x0= 1980, x1 = 2030, fillcolor ="green", opacity=0.1)
st.plotly_chart(fig_NUM_RATING)

# Ajouter espaces
st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<p style="color: #333333; font-size: 18px;">Ce graphique nous donne le nombre de vote par année de sortie de films</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px; ">Nous pouvons voir que les votes dans les années 1980 augmente fortement, certainement grace l\'utilisation d\'Internet et la croissance d\'IMDb en tant que site Web populaire pour les informations et les critiques de films, l\'augmentation de la production de films depuis les années 1980 signifie qu\'il y a tout simplement plus de films qui sortent chaque année, augmentation de la participation des cinéphiles qui utilisent Internet pour partager leur opinion sur les films</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Ce qui explique notre choix d\'orienter notre algorythme de recommendation sur les années 1980 à 2023</p>', unsafe_allow_html=True)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

############ kpi 2 ############ 

# kpi 2 Lucas
# code dataframe
df_RELEASE["startYear"] = pd.to_datetime(df_RELEASE["startYear"], format="%Y")
df_RELEASE["Annees"] = df_RELEASE["startYear"].dt.year // 10 * 10

df_pivot_RELEASE = df_RELEASE.pivot_table(columns="titleType", values="titleType", index="Annees", aggfunc="count")
df_pivot_RELEASE.reset_index(inplace=True)
df_pivot_RELEASE["tvSeries"].fillna(0, inplace=True)
df_pivot_RELEASE = df_pivot_RELEASE[df_pivot_RELEASE["Annees"] >= 1900]
df_pivot_RELEASE = df_pivot_RELEASE[df_pivot_RELEASE["Annees"] <= 2022]


# code kpi
fig_RELEASE = go.Figure()

fig_RELEASE.add_trace(go.Scatter(
    x=df_pivot_RELEASE["Annees"],
    y=df_pivot_RELEASE["movie"],
    name="Movies",
    line=dict(color="#A267AC")
))

fig_RELEASE.add_trace(go.Scatter(
    x=df_pivot_RELEASE["Annees"],
    y=df_pivot_RELEASE["tvSeries"],
    name="TV Series",
    line=dict(color="#ECA869")
))

fig_RELEASE.update_layout(
    title="Nombre de sortie de films & series",
    xaxis=dict(title="Years"),
    yaxis=dict(title="Release Count"),
    plot_bgcolor="white",
    showlegend=True,
    width=1400, height=550
)

frames = [go.Frame(data=[go.Scatter(
    x=df_pivot_RELEASE["Annees"][:i],
    y=df_pivot_RELEASE["movie"][:i],
    name="Movies",
    line=dict(color="#A267AC")
),
    go.Scatter(
        x=df_pivot_RELEASE["Annees"][:i],
        y=df_pivot_RELEASE["tvSeries"][:i],
        name="TV Series",
        line=dict(color="#ECA869")
    )],
    layout=dict(title_text=f"Number of Movies & TV Series Released (Year: {df_pivot_RELEASE['Annees'][i]})")
) for i in range(1, len(df_pivot_RELEASE))]

fig_RELEASE.update(frames=frames)

buttons = [
    dict(
        label="Play",
        method="animate",
        args=[None, {"frame": {"duration": 500, "redraw": False}, "fromcurrent": True}]
    ),
    dict(
        label="Pause",
        method="animate",
        args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}]
    )
]

fig_RELEASE.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=buttons,
            direction="left",
            x=0.1,
            y=0,
            xanchor="right",
            yanchor="top"
        )
    ]
)
st.plotly_chart(fig_RELEASE)



st.markdown('<p style="color: #333333; font-size: 18px;">L\'augmentation du nombre de films et de séries produits à partir des années 1985 peut être attribuée à plusieurs facteurs :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px; text-decoration: underline;">1. Évolution de l\'industrie cinématographique : </p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Avancées technologiques importantes, telles que l\'émergence de la vidéo et des formats de distribution plus accessibles et donc facilité de production et de diffusion +++ des films et séries.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px; text-decoration: underline;">2. Diversification des canaux de distribution :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Avec l\'essor des chaînes de télévision par câble et par satellite, l\'émergence des plateformes de streaming et l\'augmentation des opportunités de diffusion et de monétisation des contenus. </p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px; text-decoration: underline;">3. Marché mondial en expansion :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">L\'industrie cinématographique s\'est de plus en plus tournée vers le marché international, avec une demande croissante de films et de séries provenant de divers pays ce qui a permit de nouvelles opportunités commerciales et stimulé la production à grande échelle. </p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px ; text-decoration: underline;">4. Évolution des goûts et des attentes du public :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Les années 1980 ont été marquées par l\'émergence de genres populaires tels que les films d\'action, les comédies et les films de science-fiction. Ces genres ont connu un grand succès et ont influencé les choix des producteurs pour répondre à la demande du public.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px; text-decoration: underline;">5. La baisse en 2020 : COVID</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Fermeture des salles de cinéma, Restrictions de production et Confinements.</p>', unsafe_allow_html=True)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)



############ kpi 3 ############ 


# Mapping des valeurs uniques de titleType à des couleurs pastel
colors_mapping = {
    'short': 'rgb(255, 152, 152)',
    'movie': 'rgb(152, 152, 255)',
    'tvMovie': 'rgb(152, 255, 152)',
    'tvSeries': 'rgb(255, 255, 152)'
}  # Ajoutez les autres valeurs uniques de titleType avec leurs couleurs correspondantes

# Créer le graphique interactif avec Plotly
fig = px.scatter(top_titleTypes, x='Decade', y='Count', color='titleType',width=1400, height=550, color_discrete_map=colors_mapping, size='Count')
fig.update_traces(marker=dict(size=20))

# Personnaliser les étiquettes des axes et le titre
fig.update_layout(
    xaxis_title='Décennie',
    yaxis_title='Somme des films par type de diffusion',
    title='Graphique interactif par décennie'
)
st.plotly_chart(fig)


st.markdown('<p style="color: #333333; font-size: 18px;">Au fil des décennies, l\'industrie du divertissement a connu une évolution remarquable. En examinant les principales catégories de vidéos diffusées, nous pouvons observer certaines tendances intéressantes. Voici un aperçu des faits marquants :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">1. Court métrage (1860-1890) : </p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Au tout début de l\'histoire de la vidéo, les courts métrages étaient les seules formes de contenu diffusées. Ces vidéos brèves ont ouvert la voie à l\'exploration de nouveaux moyens de narration visuelle.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">2. Films cinéma (1890-1920) :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Vers les années 1890, les premiers films de cinéma sont apparus, marquant ainsi une étape majeure dans l\'industrie du divertissement. Le grand écran est devenu un lieu privilégié pour raconter des histoires et captiver les spectateurs.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">3. Films TV (1920-1940) :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Dans les années 1920, les films destinés à la télévision ont commencé à se développer. Cette nouvelle forme de divertissement a offert aux téléspectateurs la possibilité de profiter du cinéma dans le confort de leur foyer.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">4. Séries TV (1940-présent)</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Séries TV (1940-présent) : À partir des années 1940, les séries TV ont fait leur apparition. Elles sont rapidement devenues un pilier du divertissement, offrant des récits longs et complexes qui ont captivé les téléspectateurs.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Ainsi, en examinant les principales catégories de vidéos diffusées au fil du temps, on constate que le cinéma, les court métrages et les séries TV ont joué un rôle essentiel dans l\'évolution de l\'industrie du divertissement. Les séries TV, en particulier, ont connu une croissance significative et devraient continuer à gagner en popularité à l\'avenir.</p>', unsafe_allow_html=True)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)



############ kpi 4 & 5 ############ 



# Compter le nombre de titres par genre principal
genre_counts = df_HE['genre principal'].value_counts()

# Calculer le pourcentage de titres par genre principal
genre_percentages = genre_counts / len(df_HE) * 100

# Sélectionner les 5 genres principaux avec le plus grand nombre de titres
top_genres = genre_percentages.head(5)

# Créer la figure et le graphique en barres
fig2 = px.bar(top_genres, x=top_genres.index, y='genre principal',width=1400, height=550, color=top_genres.index,
             color_discrete_map={
                "Drama": "#B5DEFF",
                "Comedy": "#F7C8E0",
                "Documentary": "#ECA869",
                "Action": "#DDFFBB",
                "Adventure": "#A267AC"},
             labels={'x': 'Genre Principal', 'genre principal': 'Pourcentage de titres'},)

# Ajouter les étiquettes des pourcentages au-dessus des barres
fig2.update_traces(texttemplate='%{y:.1f}%', textposition='outside')

# Personnaliser le graphique
fig2.update_layout(title='Pourcentage des genres principaux de 1980 à 2023',
                  xaxis_title='Genre Principal',
                  yaxis_title='Pourcentage de titres',
                  showlegend=False)

# Afficher le graphique
st.plotly_chart(fig2)

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

# Compter le nombre de titres par décennie et par genre principal
genre_counts_decade = df_HE.groupby(['decade', 'genre principal']).size().unstack(fill_value=0)

# Sélectionner les 5 genres principaux avec le plus grand nombre de titres
top_genres = genre_counts_decade.sum().nlargest(5).index

# Calculer le pourcentage de titres par genre principal et par décennie
genre_percentages = genre_counts_decade[top_genres].div(genre_counts_decade.sum(axis=1), axis=0) * 100

# Créer l'histogramme empilé avec Plotly Express
fig3 = px.bar(genre_percentages, x=genre_percentages.index, y=top_genres,width=1300, height=550,
             color_discrete_map={
                "Drama": "#BFA2DB",
                "Comedy": "#A7E9AF",
                "Documentary": "#FCFFA6",
                "Action": "#FF87CA",
                "Adventure": "#6886C5"},
             labels={'x': 'Décennie', 'value': 'Pourcentage de titres'},
             title='Pourcentage de titres des 5 genres par décennie')

# Personnaliser l'histogramme empilé
fig3.update_layout(xaxis={'tickmode': 'array', 'tickvals': [1980, 1990, 2000, 2010], 'ticktext': ['1980s', '1990s', '2000s', '2010s']},
                  yaxis_range=[0, 100])

# Personnaliser l'histogramme empilé
fig3.update_layout(xaxis_title='Décennie')

# Afficher le graphique
st.plotly_chart(fig3)



st.markdown('<p style="color: #333333; font-size: 18px;">Les classements des genres les mieux notés sur IMDb de 1980 à 2023 offrent un aperçu fascinant des préférences du public.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">Voici quelques exemples de films emblématiques de chaque genre :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Drama (Drame) : "Les Évadés", "Forrest Gump", "The Dark Knight", "Fight Club", "La La Land".</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Comedy (Comédie) : "Y a-t-il un pilote dans l\'avion ?", "Le Golf en folie", "Very Bad Trip", "Mes meilleures amies", "SuperGrave".', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Documentary (Documentaire) : "Bowling for Columbine", "La Marche de l\'empereur", "Blackfish", "Amy", "Free Solo".</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Action (Action) : "Die Hard", "The Terminator", "Mad Max: Fury Road" (Mad Max: Fury Road), "The Matrix", "John Wick".</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Adventure (Aventure) : "Indiana Jones", "Le Seigneur des anneaux", "Jurassic Park", "Harry Potter", "Avatar".</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Ces films emblématiques ont captivé les spectateurs avec leur narration captivante, leurs performances mémorables et leur impact culturel, contribuant à la richesse et à la diversité du cinéma au cours de cette période.</p>', unsafe_allow_html=True)

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


############ kpi 6 ############ 

# kpi 2 Antho
# code dataframe
nouvelles_colonnes = {'Unnamed: 0': 'Name', 'personne': 'Nb_films'}
kpi_top_nbfilm = kpi_top_nbfilm.rename(columns=nouvelles_colonnes)
kpi_top_nbfilm = kpi_top_nbfilm.head(5)
#code kpi
fig_D2 = px.bar(kpi_top_nbfilm, x='Name', y='Nb_films', color='Name', width=1400, height=550,
             color_discrete_map={
                                "Christopher Nolan": "#BFA2DB",
                                "Quentin Tarantino": "#A7E9AF",
                                "Steven Spielberg": "#FCFFA6",
                                "Martin Scorsese": "#FF87CA",
                                "Peter Jackson": "#6886C5",})                  

fig_D2.update_layout(
    title='Top 5 Réalisateurs par nombre de film', 
    plot_bgcolor='white',
    showlegend = False,
    
    xaxis = dict(
        title='Directors', 
        showgrid=True, 
        rangeslider = dict(
            visible=True, 
            thickness=0.02)), 
    
    yaxis = dict(
        title='Films', 
        mirror=True,
        ticks='outside',
        showline=True,
        linecolor='lightgrey',
        gridcolor='lightgrey',), 
    
        barmode='relative', 
    )

fig_D2.update_yaxes(range=[0, 8],
                mirror=True,
                ticks='outside',
                showline=True,
                linecolor='lightgrey',
                gridcolor='lightgrey')

fig_D2.update_traces(texttemplate='%{y:.f}', textposition='inside')

st.plotly_chart(fig_D2)


st.markdown('<p style="color: #333333; font-size: 18px;">Ce classement n\'est pas surprenant car durant cette période, les réalisateurs suivants ont produit un certain nombre de films remarquables :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">1. Christopher Nolan :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Avec des films tels que "Inception", qui a remporté plusieurs récompenses et a été un énorme succès au box-office, ainsi que "Interstellar" et bien sûr "The Dark Knight" et "Dunkirk", Nolan a su captiver les spectateurs avec ses histoires complexes et visuellement impressionnantes.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">2. Quentin Tarantino :', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Tarantino a réalisé des films emblématiques tels que "Reservoir Dogs", qui a marqué ses débuts réussis, et surtout "Pulp Fiction", qui a remporté de nombreux prix prestigieux et est considéré comme un classique du cinéma. Sa saga "Kill Bill" a également connu un grand succès et a été saluée pour son style unique et sa narration captivante.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">3. Steven Spielberg :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Spielberg a offert au public des films inoubliables comme "E.T. l\'extra-terrestre" et "Jurassic Park", qui sont encore aujourd\'hui des références du cinéma. Ces films ont non seulement connu un immense succès commercial, mais ont également remporté des récompenses et sont devenus des films cultes.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">4. Martin Scorsese :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Scorsese a réalisé des films mémorables tels que "Taxi Driver", qui a été salué par la critique et a remporté des prix, ainsi que des films comme "Goodfellas", "The Departed" et "Raging Bull", qui ont été acclamés pour leur réalisation brillante et leurs performances d\'acteurs.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;text-decoration: underline;">5. Peter Jackson :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Jackson a hissé les histoires de Tolkien au sommet du box-office avec sa trilogie "Le Seigneur des Anneaux". Ces films ont non seulement connu un énorme succès commercial, mais ont également remporté de nombreux prix, dont plusieurs Oscars, pour leur réalisation épique et leur fidélité à l\'œuvre originale.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Ces réalisateurs ont su marquer cette période avec leurs films emblématiques, leur créativité et leur capacité à captiver les spectateurs. Ils ont laissé une empreinte indélébile dans l\'histoire du cinéma.</p>', unsafe_allow_html=True)
            
            
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


############ kpi 7 ############ 

# kpi 1 Antho
# code dataframe
kpi_top_ratings = kpi_top_ratings.head(5)
# code kpi
fig_D1 = px.bar(kpi_top_ratings, x='Name', y='Ratings', color='Name', width=1400, height=550,
             color_discrete_map={
                                "Frank Darabont": "#B5DEFF",
                                "Peter Jackson": "#F7C8E0",
                                "Lilly Wachowski": "#ECA869",
                                "Irvin Kershner": "#DDFFBB",
                                "Lana Wachowski": "#A267AC"})

fig_D1.update_layout(
    title='Top 5 Réalisateurs par note moyenne', 
    plot_bgcolor='white',
    showlegend = False,
    
    xaxis = dict(
        title='Directors', 
        showgrid=True, 
        rangeslider = dict(
            visible=True, 
            thickness=0.08)), 
    
    yaxis = dict(
        title='Rating', 
        mirror=True,
        ticks='outside',
        showline=True,
        linecolor='lightgrey',
        gridcolor='lightgrey',), 
    
    barmode='relative', 
    )
fig_D1.update_yaxes(range=[7, 9.5],
                mirror=True,
                ticks='outside',
                showline=True,
                linecolor='lightgrey',
                gridcolor='lightgrey')
fig_D1.update_traces(texttemplate='%{y:.2f}', textposition='inside')

st.plotly_chart(fig_D1)


st.markdown('<p style="color: #333333;  font-size: 18px;">Durant la période de 1980 à 2010, certains réalisateurs ont su conquérir le cœur du public avec leurs films remarquables et ont obtenu des notes élevées. Voici les réalisateurs qui ont reçu les meilleures notes :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333;  font-size: 18px;text-decoration: underline;">1. Franck Darabont : </p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333;  font-size: 18px;">Avec une note impressionnante de 9.07 sur 10, Franck Darabont s\'est démarqué grâce à ses films captivants et émotionnellement puissants. Son chef-d\'œuvre "Les Évadés" a été salué par la critique et a conquis le public avec son histoire poignante et ses performances exceptionnelles.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333;  font-size: 18px;text-decoration: underline;">2. Peter Jackson :', unsafe_allow_html=True)
st.markdown('<p style="color: #333333;  font-size: 18px;">Avec une note de 8.87 sur 10, Peter Jackson a su transporter les spectateurs dans des mondes fantastiques. Sa trilogie épique "Le Seigneur des Anneaux", adaptée des romans de J.R.R. Tolkien, a été acclamée pour sa réalisation grandiose, ses effets spéciaux révolutionnaires et son casting brillant.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333;  font-size: 18px;text-decoration: underline;">3. Lilly Wachowski, Lana Wachowski et Irvin Kershner :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333;  font-size: 18px;">Ces trois réalisateurs ont tous obtenu une note équivalente de 8.70 sur 10. Lilly et Lana Wachowski ont impressionné avec leur vision innovante et audacieuse dans la trilogie "Matrix", qui a redéfini les limites du genre de la science-fiction. Quant à Irvin Kershner, il a réalisé "Star Wars : Épisode V - L\'Empire contre-attaque", considéré comme l\'un des meilleurs volets de la saga "Star Wars".</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333;  font-size: 18px;">Ces réalisateurs ont su séduire le public grâce à leur talent, leur créativité et leur capacité à raconter des histoires captivantes. Leurs films ont marqué cette période et continuent d\'être appréciés par de nombreux cinéphiles.</p>', unsafe_allow_html=True)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)



############ kpi 7 ############ 

# kPI3 Chrysanthe
# code dataframe
df10=df.sort_values(by='note', ascending=False).head(10)
# code kpi
#Top des 10 films les mieux notés de 1980 à 2023 

fig8 = px.histogram(df10, x="titre", y="note", color="genre_principal",
                   title="Top 10 des films les mieux notés de 1980 à 2023",
                   hover_data=["numVotes"],
                   color_discrete_sequence=px.colors.qualitative.Pastel)
fig8.update_layout(xaxis_title="Titre de film", yaxis_title="Note",
                  height=600, width=1400, yaxis=dict(range=[8, 10]))
fig8.update_xaxes(categoryarray=df10['titre'])
st.plotly_chart(fig8)

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


st.markdown('<p style="color: #333333; font-size: 18px;">Durant la période de 1980 à 2010, le public a témoigné son amour pour certains films qui ont reçu des notes exceptionnelles. Il n\'est donc pas surprenant de retrouver les films des réalisateurs qui ont également obtenu les meilleures notes. Voici un aperçu des films les plus aimés par le public durant cette période :</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Parmi les réalisateurs mentionnés précédemment, plusieurs de leurs films se démarquent parmi les favoris du public. Tout d\'abord, Franck Darabont a réussi à captiver les spectateurs avec son film "Les Évadés", qui a obtenu une note élevée. De même, Peter Jackson a conquis les cœurs avec sa trilogie épique "Le Seigneur des Anneaux", qui figure parmi les films les mieux notés. "La Liste de Schindler", réalisé par Steven Spielberg, a ému et marqué les esprits avec son récit poignant sur l\'Holocauste. "The Dark Knight" de Christopher Nolan a été acclamé pour sa vision sombre et complexe de Batman. "Pulp Fiction" de Quentin Tarantino a fait sensation avec son style unique et ses dialogues percutants. "Inception" de Christopher Nolan, qui a repoussé les limites de la réalité et de l\'intrigue, ainsi que "Fight Club" de David Fincher, qui a captivé les spectateurs avec son scénario audacieux et ses performances remarquables. Enfin, "Forrest Gump" de Robert Zemeckis a touché les cœurs avec son récit émouvant et son personnage emblématique.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Ces films, portés par des réalisateurs talentueux, ont su rassembler un large public et continuent d\'être appréciés pour leur qualité artistique, leurs performances exceptionnelles et leurs histoires captivantes. Ils ont laissé une empreinte indélébile dans l\'histoire du cinéma et continuent de faire partie des favoris des cinéphiles du monde entier.</p>', unsafe_allow_html=True)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)



############ kpi 8 ############ 



# kpi5 Chrysanthe
# code dataframe
# Sélectionner les données pour les acteurs et les actrices
df_actors = df[df['job'] == 'actor']
df_actresses = df[df['job'] == 'actress']
# Calculer le nombre total de films et la note moyenne pour chaque acteur et chaque actrice
df_actors_summary = df_actors.groupby(['nconst', 'personne'], as_index=False).agg({'nb_films': 'sum', 'note': 'mean'})
df_actresses_summary = df_actresses.groupby(['nconst', 'personne'], as_index=False).agg({'nb_films': 'sum', 'note': 'mean'})
# Trier les données par ordre décroissant de nombre de films puis de note moyenne
df_actors_summary = df_actors_summary.sort_values(['nb_films', 'note'], ascending=[False, False])
df_actresses_summary = df_actresses_summary.sort_values(['nb_films', 'note'], ascending=[False, False])
# Sélectionner les 5 acteurs ayant le plus grand nombre de films et la meilleure note moyenne
top_actors = df_actors_summary.head(5)
# Sélectionner les 5 actrices ayant le plus grand nombre de films et la meilleure note moyenne
top_actresses = df_actresses_summary.head(5)
# code kpi
# Créer un graphique de barres pour les 5 acteurs
fig_actors = px.bar(top_actors, x='personne', y='nb_films', color='note')
fig_actors.update_xaxes(title='Acteur')
fig_actors.update_yaxes(title='Nombre de films')
fig_actors.update_traces(texttemplate='%{y}', textposition='outside')
fig_actors.update_layout(paper_bgcolor='rgba(240, 240, 240, 0.85)', plot_bgcolor='rgba(240, 240, 240, 0.85)')
# Créer un graphique de barres pour les 5 actrices
fig_actresses = px.bar(top_actresses, x='personne', y='nb_films', color='note')
fig_actresses.update_xaxes(title='Actrice')
fig_actresses.update_yaxes(title='Nombre de films')
fig_actresses.update_traces(texttemplate='%{y}', textposition='outside')
fig_actresses.update_layout(paper_bgcolor='rgba(240, 240, 240, 0.85)', plot_bgcolor='rgba(240, 240, 240, 0.85)')
# Afficher les graphiques côte à côte
fig3 = sp.make_subplots(rows=1, cols=2)

fig3.add_trace(fig_actors['data'][0], row=1, col=1)
fig3.add_trace(fig_actresses['data'][0], row=1, col=2)


fig3.update_xaxes(showgrid=False, zeroline=False, title_text="Acteur / Actrice")
fig3.update_yaxes(showgrid=False, zeroline=False,title_text="Nombres de films")

fig3.update_layout(width=1400, height=500, 
    title="Nombre de films par Acteur/Actrice, couleurs par note moyenne",  title_x=0.3)


st.plotly_chart(fig3)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


# code dataframe
# Sélectionner les données pour les acteurs et les actrices
df_actors = df[df['job'] == 'actor']
df_actresses = df[df['job'] == 'actress']
# Filtrer les données pour chaque décennie
decades = [1980, 1990, 2000, 2010]
top_performers = []
for decade in decades:
    df_decade_actors = df_actors[df_actors['decennie'] == decade]
    df_decade_actresses = df_actresses[df_actresses['decennie'] == decade]
    # Trouver l'acteur et l'actrice avec la meilleure note moyenne et le plus grand nombre de films
    top_actor = df_decade_actors.sort_values(['note', 'nb_films'], ascending=[False, False]).iloc[0]
    top_actress = df_decade_actresses.sort_values(['note', 'nb_films'], ascending=[False, False]).iloc[0]
    # Ajouter ces informations à une liste pour chaque décennie
    top_performers.append({'decennie': decade, 'actor': top_actor, 'actress': top_actress})
# code kpi
# Créer la figure avec des sous-graphes
fig4 = sp.make_subplots(rows=2, cols=2, subplot_titles=("1980s", "1990s", "2000s", "2010s"))

# Ajouter les graphiques de barres pour chaque décennie et chaque sexe
for i, decade in enumerate(decades):
    row = i // 2 + 1
    col = i % 2 + 1

    # Récupérer les données pour l'acteur et l'actrice pour cette décennie
    top_actor = top_performers[i]['actor']
    top_actress = top_performers[i]['actress']

    # Créer les graphiques de barres pour l'acteur et l'actrice
    actor_bar = go.Bar(name='Meilleur acteur', x=[top_actor['personne']], y=[top_actor['note']],
                       marker_color='rgb(167, 232, 236)')
    actress_bar = go.Bar(name='Meilleure actrice', x=[top_actress['personne']], y=[top_actress['note']],
                         marker_color='rgb(223, 163, 240)')

    # Ajouter les graphiques de barres à la figure
    fig4.add_trace(actor_bar, row=row, col=col)
    fig4.add_trace(actress_bar, row=row, col=col)

    # Mettre à jour les titres des axes
    fig4.update_xaxes(title_text="Acteur/Actrice", row=row, col=col)
    fig4.update_yaxes(title_text="Note", row=row, col=col)

# Mettre à jour le titre global de la figure
fig4.update_layout(width=1400, height=700, title_x=0.4)
fig4.update_layout(title_text="Meilleurs acteur et actrice par décennie",showlegend = False)

st.plotly_chart(fig4)

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown('<p style="color: #333333; font-size: 18px;">Au cours de la période allant de 1980 à 2010, certains acteurs et actrices ont su captiver le public par leurs performances remarquables et ont ainsi obtenu les meilleures notes.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">Ces cinq acteurs et ces cinq actrices ont marqué l\'industrie cinématographique de 1980 à 2010 par leurs performances exceptionnelles et leur capacité à toucher le cœur du public. Leur talent et leur dévouement leur ont valu une place privilégiée dans le cœur des cinéphiles du monde entier. Que ce soit par leurs rôles iconiques, leurs prestations émouvantes ou leur capacité à incarner des personnages inoubliables, ces acteurs et actrices ont laissé une empreinte indélébile sur le cinéma de cette période.</p>', unsafe_allow_html=True)


# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)
# Ajouter séparateur 
st.markdown(f'<div style="{separator_style}"></div>', unsafe_allow_html=True)
# Ajouter espaces
st.markdown("<br>", unsafe_allow_html=True)


#####################conclusion##################################

# Titre
st.markdown('<p style="color: #4F4F4F; font-family:Oswald; font-size: 35px; text-align: center;">CONCLUSION</p>', unsafe_allow_html=True)

# Ajouter espaces
st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<p style="color: #333333; font-size: 18px;">- Les votes IMDB pour les films sortis après 1980 ont connu une forte augmentation en raison de l\'expansion du marché et de l\'évolution du monde du cinéma, avec des franchises populaires comme Star Wars, Retour vers le futur et Le Seigneur des anneaux captivant l\'attention du public.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Cependant, en 2020, ces votes ont connu une baisse significative en raison de la pandémie de Covid-19 qui a entraîné une diminution de la fréquentation des salles de cinéma et une réduction des sorties de nouveaux films.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Malgré la popularité croissante des séries télévisées, le public de ce format est moins enclin à voter sur IMDB, ce qui explique une différence dans la représentativité des votes entre les films et les séries.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Du côté des réalisateurs, les meilleures notes IMDB ne sont pas systématiquement attribuées à ceux qui ont réalisé un grand nombre de films. Cela démontre que les producteurs privilégient davantage les projets cinématographiques porteurs plutôt que de se baser uniquement sur la popularité des réalisateurs ou leurs notes sur IMDB.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- Dans le top des films, des titres tels que "Les Évadés" continuent à être appréciés par le public malgré le passage du temps, tandis que les genres cinématographiques tels que la fantasy et les films de super-héros (comme la trilogie "Le Seigneur des anneaux" et "The Dark Knight") sont également très populaires.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; font-size: 18px;">- En ce qui concerne les acteurs et actrices, les mieux notés sur IMDB ne suivent pas la même tendance. Les acteurs établis depuis des décennies, comme Mark Hamill dans Star Wars et Tom Hanks, conservent une place de choix chez les hommes. Cependant, une jeune actrice comme Natalie Portman occupe également le haut du classement, surpassant des actrices bien installées comme Robin Wright et Linda Hamilton.</p>', unsafe_allow_html=True)








