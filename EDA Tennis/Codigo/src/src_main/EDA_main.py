#Importación de streamlit y los demas scripts
import streamlit as st
import EDA_funciones as func

#Importacion de librerias
from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

big_3_best_seasons, big3_MT, big3matches, big3serve, big3aces_DF, big3return, big3_matchtime, big3upsets,\
           h2h, big3_RGWP_final, big3_RMMP_final, big3_RMMW_final, big3_RWS_final, big3_RAR_final, big3_RATP_final,\
           opinions, GOAT_total, GOAT_hard, GOAT_clay, GOAT_grass, timeline, GS_timeline = func.load_data()

#Inicio de Streamlit

#Organización de la página con un menú lateral
st.sidebar.title('Tennis GOAT debate')
menu = st.sidebar.selectbox('Selection Menu', ('Home', 'Big Titles', 'Statistics Charts', 'Performance Charts'
                                               , 'Timelines Charts', 'Rivalries Charts', 'Records charts', 'GOAT LISTS',
                                               'Opinion', 'Conclusion', 'All charts'))

#Cada selección del menu con su información
if menu == 'Home':
    func.main()

if menu == 'Big Titles':
    st.title('Big Titles')
    st.write('Los principales parámetros que se tienen en cuenta son los denominados Big Titles.'
             '\n\nEstos son:\n\nGrand slam titles\n\nATP finals titles\n\nATP Masters titles\n\nOlympics')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/BIG_BIGTITLES.jpg')

if menu == 'All charts':
    st.title('Statistics')
    # Tabla de serve
    st.header('Big 3 Serve')
    st.write(big3serve)
    # Tabla de Aces/DF
    st.header('Big 3 Aces & DF')
    st.write(big3aces_DF)
    # Tabla de return
    st.header('Big 3 Return')
    st.write(big3return)
    # Tabla de matches time
    st.header('Big 3 Match time')
    st.write(big3_matchtime)
    # Tabla de upsets
    st.header('Big 3 Upsets')
    st.write(big3upsets)

    st.title('Performance')
    # Tabla de big 3 matches
    st.header('Big 3 Matches')
    st.write(big3matches)
    # Tabla de big 3 best seasons
    st.header('Big 3 Best seasons')
    st.write(big_3_best_seasons)
    # Tabla de big 3 mental toughness
    st.header('Big 3 Mental Toughness')
    st.write(big3_MT)

    st.title('Timelines')
    st.write(timeline)
    st.write(GS_timeline)

    st.title('Rivalries')
    #Tabla de rivalries
    st.header('Heads to heads')
    st.write(h2h)

    st.title('Records')
    # Tabla record ranking
    st.header('ATP Ranking Records')
    st.write(big3_RATP_final)
    # Tabla record Greatest %
    st.header('Greatest winning % Records')
    st.write(big3_RGWP_final)
    # Tabla record winning streaks
    st.header('Winning streaks Records')
    st.write(big3_RWS_final)
    # Tabla record most matches played
    st.header('Most matches played Records')
    st.write(big3_RMMP_final)
    # Tabla record most matches won
    st.header('Most matches won Records')
    st.write(big3_RMMW_final)
    # Tabla record all records
    st.header('All records Records')
    st.write(big3_RAR_final)

    st.title('GOAT LISTS')
    # Tabla GOAT hard
    st.header('GOAT Hard')
    st.write(GOAT_hard)
    # Tabla GOAT clay
    st.header('GOAT Clay')
    st.write(GOAT_clay)
    # Tabla GOAT grass
    st.header('GOAT Grass')
    st.write(GOAT_grass)
    # Tabla GOAT total
    st.header('GOAT Overall')
    st.write(GOAT_total)

    st.title('Opinions')
    # Tabla de opiniones
    st.header('Opinions')
    st.write(opinions)

if menu == 'Statistics Charts':
    st.title('Statistics')
    # Grafica Big 3 serve
    st.header('Big 3 Serve')
    st.write(big3serve)
    func.graph_big3serve(big3serve)
    st.write('Career First serve won %')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/grafica_1stserve_career.png')
    st.write('Source: https://www.ultimatetennisstatistics.com/statsChart#')
    st.subheader('Conclusión')
    st.write('Federer está por encima de sus competidores en cuanto'
             ' a sacar se refiere. Novak y Rafa ligeramente por detrás.')

    # Grafica Big 3 aces&df
    st.header('Big 3 Aces & Double faults')
    st.write(big3aces_DF)
    func.graph_big3aces_DF(big3aces_DF)
    st.write('Career Aces per match')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/career_acespermatch.png')
    st.write('Source: https://www.ultimatetennisstatistics.com/statsChart#')
    st.subheader('Conclusión')
    st.write('Federer claro ganador, Novak mejor que Rafa.')

    # Grafica Big 3 return
    st.header('Big 3 Return')
    st.write(big3return)
    func.graph_big3return(big3return)
    st.write('Career Second serve return won %')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/grafica_2ndreturn_career.png')
    st.write('Source: https://www.ultimatetennisstatistics.com/statsChart#')
    st.subheader('Conclusión')
    st.write('Novak y Rafa realmente parejos, destacar que Federer se encuentra '
             ' algo por detrás.')

    # Grafica Big 3 matchtime
    st.header('Big 3 Match time')
    st.write(big3_matchtime)
    func.graph_big3_matchtime(big3_matchtime)
    st.write('Career match time')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/grafica_career_match_time.png')
    st.write('Source: https://www.ultimatetennisstatistics.com/statsChart#')
    st.subheader('Conclusión')
    st.write('Federer se caracteriza por un juego más ofensivo, los datos lo demuestran'
             ' con una duración menor en la media de sus partidos.')

    # Grafica Big 3 upsets
    st.header('Big 3 Upsets')
    st.write(big3upsets)
    func.graph_big3upsets(big3upsets)

if menu == 'Performance Charts':
    st.title('Performance')
    #Grafica Big 3 matches
    st.header('Big 3 Matches')
    st.write(big3matches)
    func.graph_big3matches(big3matches)
    st.subheader('Conclusión')
    st.write('Medias muy similares de los tres jugadores.\n\nMirando detenidamente:'
             '\n\n En pista dura Djokovic es ligeramente superior a Federer. Nadal se queda por detrás.'
             '\n\n En pista de tierra Nadal es claro dominador, seguido de Djokovic. Federer se queda por detrás.'
             '\n\n En pista de hierba Federer es ligeramente superior a Djokovic. Nadal se queda por detrás.')

    #Grafica Big 3 Best seasons
    st.header('Big 3 Best seasons')
    st.write(big_3_best_seasons)
    func.graph_big_3_best_seasons(big_3_best_seasons)
    st.subheader('Conclusión')
    st.write('Destacar que los tres jugadores han conseguido 11 de las 20 mejores temporadas de la'
             ' historia del tenis. A pesar de eso, Djokovic ligeramente superior a Federer, Nadal '
             'muy por detrás.')

    #Grafica Big 3 Mental toughness
    st.header('Big 3 Mental Toughness')
    st.write(big3_MT)
    func.graph_big3_MT(big3_MT)
    st.subheader('Conclusión')
    st.write('Revelación, Djokovic mejor jugador de la historia en momentos bajo presión. Nadal y '
             'Federer bastante por detrás.')

if menu == 'Timelines Charts':
    st.title('Timelines')

    # Tabla de dominance 20 años
    st.header('Career Dominance timeline')
    st.write(timeline)
    func.graph_timeline(timeline)
    # Tabla de dominance 2002-2011
    st.header('2002-2011 Dominance timeline')
    func.graph_timeline_1(timeline)
    st.subheader('Conclusion')
    st.write('Federer dominador de la década. Nadal destaca al final, y Djokovic aparece por primera vez')
    # Tabla de dominance 2012-2021
    st.header('2012-2021 Dominance timeline')
    func.graph_timeline_2(timeline)
    st.subheader('Conclusion')
    st.write('Djokovic dominador absoluto de la última década')
    # Tabla de Grand slam dominance
    st.header('Grand slam timeline')
    st.write(GS_timeline)
    st.image('/Users/angel\OneDrive\Escritorio\EDA/GS_timelinegrafica.png')
    #func.graph_grandslam_timeline(GS_timeline)
    st.subheader('Conclusion')
    st.write('Refleja lo comentado anteriormente, primera década con Federer dominando y segunda década con Djokovic.'
             'Nadal demuestra una mayor constancia.')
    #st.image('/Users/angel\OneDrive\Escritorio\EDA/Grand_Slam_dominance.jpeg')

if menu == 'Rivalries Charts':
    st.title('Rivalries')
    # Tabla de rivalries
    st.header('Heads to heads')
    st.write(h2h)
    st.write('Head to head:\n\nNovak Djokovic se corona con la primera posición, seguido de'
             ' Rafael Nadal, y por último, Roger Federer.')

if menu == 'Records charts':
    st.title('Records')
    #Tabla record ranking
    st.header('ATP Ranking Records')
    st.write(big3_RATP_final)
    #Tabla record Greatest %
    st.header('Greatest winning % Records')
    st.write(big3_RGWP_final)
    #Tabla record winning streaks
    st.header('Winning streaks Records')
    st.write(big3_RWS_final)
    # Tabla record most matches played
    st.header('Most matches played Records')
    st.write(big3_RMMP_final)
    # Tabla record most matches won
    st.header('Most matches won Records')
    st.write(big3_RMMW_final)
    # Tabla record all records
    st.header('All records Records')
    st.write(big3_RAR_final)

if menu == 'GOAT LISTS':
    st.title('GOAT LISTS')
    #Tabla GOAT hard
    st.header('GOAT Hard')
    st.write(GOAT_hard)
    # Tabla GOAT clay
    st.header('GOAT Clay')
    st.write(GOAT_clay)
    #Tabla GOAT grass
    st.header('GOAT Grass')
    st.write(GOAT_grass)
    #Tabla GOAT total
    st.header('GOAT Overall')
    st.write(GOAT_total)

if menu == 'Opinion':
    st.title('Opinion')
    # Grafica Big 3 opiniones
    st.header('Big 3 Opinions')
    st.write(opinions)
    st.image('/Users/angel\OneDrive\Escritorio\EDA/opiniones_grafico.png')

if menu == 'Conclusion':
    st.title('Conclusion')
    st.header('Objetividad')
    st.write('Como han demostrado los datos, Novak Djokovic despues de conseguir Wimbledon y sumar 20 grand slams le '
             'arrebata el trono a Federer y se situa como el mejor jugador de todos los tiempos. Nadal ligeramente por'
             ' detras de ellos.  ')
    st.header('Subjetividad')
    st.write('Por parte de los fans, Federer sigue siendo el gran favorito. Djokovic ya se sitúa en segunda posición '
             'recortando las distancias con el suizo. Nadal se queda como el tercer mejor jugador de la historia.')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/djokovic_image.png')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/federer_image.png')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/nadal_image.png')



