import streamlit as st
import pandas as pd
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
init_notebook_mode(connected=True)

def load_data():
    # Lectura de los CSV
    # CSV Performance
    big_3_best_seasons = pd.read_csv('big_3_best_seasons.csv')
    big3_MT = pd.read_csv('big3_MT.csv')
    big3matches = pd.read_csv('big3matches.csv')

    # CSV Statistics
    big3serve = pd.read_csv('big3serve.csv')
    big3aces_DF = pd.read_csv('big3aces_DF.csv')
    big3return = pd.read_csv('big3return.csv')
    big3_matchtime = pd.read_csv('big3_matchtime.csv')
    big3upsets = pd.read_csv('big3upsets.csv')

    # CSV Rivalries
    h2h = pd.read_csv('h2h.csv')

    # CSV Records
    big3_RGWP_final = pd.read_csv('big3_RGWP_final.csv')
    big3_RMMP_final = pd.read_csv('big3_RMMP_final.csv')
    big3_RMMW_final = pd.read_csv('big3_RMMW_final.csv')
    big3_RWS_final = pd.read_csv('big3_RWS_final.csv')
    big3_RAR_final = pd.read_csv('big3_RAR_final.csv')
    big3_RATP_final = pd.read_csv('big3_RATP_final.csv')

    # Opinions
    opinions = pd.read_csv('opinions.csv')

    # GOAT lists
    GOAT_total = pd.read_csv('GOATtotal.csv')
    GOAT_hard = pd.read_csv('GOAThard.csv')
    GOAT_clay = pd.read_csv('GOATclay.csv')
    GOAT_grass = pd.read_csv('GOATgrass.csv')

    # Timeline
    timeline = pd.read_csv('timeline.csv')
    GS_timeline = pd.read_csv('GS_timeline.csv')

    return big_3_best_seasons, big3_MT, big3matches, big3serve, big3aces_DF, big3return, big3_matchtime, big3upsets,\
           h2h, big3_RGWP_final, big3_RMMP_final, big3_RMMW_final, big3_RWS_final, big3_RAR_final, big3_RATP_final,\
           opinions, GOAT_total, GOAT_hard, GOAT_clay, GOAT_grass, timeline, GS_timeline

def main():
    @st.cache(persist=False)
    def csv_loader():
        st.balloons()
    st.title('TENNIS GOAT')
    st.header('Who deserves the crown?')
    st.write(' ')
    st.image('/Users/angel\OneDrive\Escritorio\EDA/big3_202020.jpg')
    st.write(' ')
    st.write('Puntos a seguir en el EDA:')
    st.write(
        "Lo primero, parámetros principales a tener en cuenta para llegar a entrar en el debate. \n\nA continuación, "
        "entraremos en la parte analítica del proyecto donde desde un enfoque objetivo sacaremos unas conclusiones. "
        "\n\nEn esta parte veremos: \n\nEstadísticas y rendimiento de sus respectivas carreras tenísticas.\n\nLineas "
        "temporales (dominancia y ranking).\n\nRivalidades. \n\nPor otro lado, valoraremos las opiniones de la gente, "
        "es decir, enfoque subjetivo.")

def graph_big3matches(big3matches):
    trace1 = go.Bar(x=big3matches['name'],
                    y=[83.30, 83.20, 81.91],
                    name='Pct Total',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3matches['Pct Total'])
    trace2 = go.Bar(x=big3matches['name'],
                    y=[84.44, 77.96, 83.26],
                    name='Pct Hard',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3matches['Pct Hard'])
    trace3 = go.Bar(x=big3matches['name'],
                    y=[80.53, 91.52, 76.09],
                    name='Pct Clay',
                    marker=dict(color='rgba(255, 150, 56, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3matches['Pct Clay'])
    trace4 = go.Bar(x=big3matches['name'],
                    y=[85.00, 78.02, 86.88],
                    name='Pct Grass',
                    marker=dict(color='rgba(80, 150, 230, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3matches['Pct Grass'])
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(barmode="group", title='Big 3 Matches Performance')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_big_3_best_seasons(big_3_best_seasons):
    trace1 = go.Bar(x=big_3_best_seasons['country_id'],
                    y=[5],
                    name='Novak Djokovic',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text='Novak Djokovic')
    trace2 = go.Bar(x=big_3_best_seasons['country_id'],
                    y=[2],
                    name='Rafael Nadal',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text='Rafael Nadal')
    trace3 = go.Bar(x=big_3_best_seasons['country_id'],
                    y=[4],
                    name='Roger Federer',
                    marker=dict(color='rgba(255, 150, 56, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text='Roger Federer')
    data = [trace1, trace2, trace3]
    layout = go.Layout(barmode="group", title='Big 3 Best Seasons')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_big3_MT(big3_MT):
    trace1 = go.Bar(x=big3_MT['name'],
                    y=[70.0, 70.4, 66.0],
                    name='Finals Pct',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_MT['finalsPct'])
    trace2 = go.Bar(x=big3_MT['name'],
                    y=[64.6, 60.5, 65.3],
                    name='TieBreak Pct',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_MT['tieBreaksPct'])
    trace3 = go.Bar(x=big3_MT['name'],
                    y=[73.4, 69.1, 64.4],
                    name='Deciding Set Pct',
                    marker=dict(color='rgba(255, 150, 56, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_MT['decidingSetsPct'])
    trace4 = go.Bar(x=big3_MT['name'],
                    y=[69.2, 54.1, 56.3],
                    name='Deciding Set Tiebreak Pct',
                    marker=dict(color='rgba(80, 150, 230, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_MT['decidingSetTieBreaksPct'])
    trace5 = go.Bar(x=big3_MT['name'],
                    y=[77.3, 64.7, 57.4],
                    name='Fifth Set Pct',
                    marker=dict(color='rgba(80, 80, 80, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_MT['fifthSetsPct'])
    data = [trace1, trace2, trace3, trace4, trace5]
    layout = go.Layout(barmode="group", title='Big 3 Mental toughness')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_big3serve(big3serve):
    trace1 = go.Bar(x=big3serve['name'],
                    y=[73.60, 72.15, 77.42],
                    name='1st serve won %',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3serve['1st serve won %'])
    trace2 = go.Bar(x=big3serve['name'],
                    y=[55.41, 57.43, 57.02],
                    name='2nd serve won %',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3serve['2nd serve won %'])
    trace3 = go.Bar(x=big3serve['name'],
                    y=[64.90, 68.21, 62.12],
                    name='1st Serve %',
                    marker=dict(color='rgba(255, 150, 56, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3serve['1st Serve %'])
    trace4 = go.Bar(x=big3serve['name'],
                    y=[65.33, 66.42, 67.30],
                    name='BP saved %',
                    marker=dict(color='rgba(80, 150, 230, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3serve['BP saved %'])
    data = [trace3, trace1, trace2, trace4]
    layout = go.Layout(barmode="group", title='Big 3 Serve Statistics')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_big3aces_DF(big3aces_DF):
    trace1 = go.Bar(x=big3aces_DF['name'],
                    y=big3aces_DF['Aces'],
                    name='Aces',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3aces_DF['Aces'])
    trace2 = go.Bar(x=big3aces_DF['name'],
                    y=big3aces_DF['DF'],
                    name='DF',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3aces_DF['DF'])
    data = [trace1, trace2]
    layout = go.Layout(barmode="group", title='Big 3 Aces & Double Faults')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_big3return(big3return):
    trace1 = go.Bar(x=big3return['name'],
                    y=[33.77, 34.24, 32.37],
                    name='Return 1st won %',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3return['Return 1st won %'])
    trace2 = go.Bar(x=big3return['name'],
                    y=[55.16, 55.28, 50.66],
                    name='Return 2nd won %',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3return['Return 2nd won %'])
    trace3 = go.Bar(x=big3return['name'],
                    y=[42.20, 42.40, 39.57],
                    name='Return won %',
                    marker=dict(color='rgba(255, 150, 56, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3return['Return won %'])
    trace4 = go.Bar(x=big3return['name'],
                    y=[44.39, 44.98, 41.16],
                    name='BP won %',
                    marker=dict(color='rgba(80, 150, 230, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3return['BP won %'])
    data = [trace3, trace1, trace2, trace4]
    layout = go.Layout(barmode="group", title='Big 3 Return Statistics')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_big3_matchtime(big3_matchtime):
    trace1 = go.Bar(x=big3_matchtime['name'],
                    y=[1.51, 1.53, 1.39],
                    name='Match time',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_matchtime['Match Time'])
    trace2 = go.Bar(x=big3_matchtime['name'],
                    y=[1.46, 1.53, 1.39],
                    name='Match time hard',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_matchtime['Match Time Hard'])
    trace3 = go.Bar(x=big3_matchtime['name'],
                    y=[1.58, 1.50, 1.45],
                    name='Match time clay',
                    marker=dict(color='rgba(255, 150, 56, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_matchtime['Match Time Clay'])
    trace4 = go.Bar(x=big3_matchtime['name'],
                    y=[2.05, 2.13, 1.42],
                    name='Match time grass',
                    marker=dict(color='rgba(80, 150, 230, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3_matchtime['Match Time Grass'])
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(barmode="group", title='Big 3 Match Time')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_big3upsets(big3upsets):
    trace1 = go.Bar(x=big3upsets['name'],
                    y=[139, 157, 198],
                    name='Victoria como no favorito',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3upsets['Victoria como no favorito'])
    trace2 = go.Bar(x=big3upsets['name'],
                    y=[59, 57, 77],
                    name='Derrota como favorito',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=big3upsets['Derrota como favorito'])
    data = [trace1, trace2]
    layout = go.Layout(barmode="group", title='Big 3 upsets')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_timeline(timeline):
    trace1 = go.Bar(x=[2002],
                    y=[1],
                    name='Hewitt',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][0])
    trace2 = go.Bar(x=[2003],
                    y=[1],
                    name='Roddick',
                    marker=dict(color='rgba(50, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][1])
    trace3 = go.Bar(x=[2004],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][2])
    trace4 = go.Bar(x=[2005],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][3])
    trace5 = go.Bar(x=[2006],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][4])
    trace6 = go.Bar(x=[2007],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][5])
    trace7 = go.Bar(x=[2008],
                    y=[1],
                    name='Nadal',
                    marker=dict(color='rgba(250, 100, 45, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][6])
    trace8 = go.Bar(x=[2009],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][7])
    trace9 = go.Bar(x=[2010],
                    y=[1],
                    name='Nadal',
                    marker=dict(color='rgba(250, 100, 45, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][8])
    trace10 = go.Bar(x=[2011],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][9])
    trace11 = go.Bar(x=[2012],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][10])
    trace12 = go.Bar(x=[2013],
                     y=[1],
                     name='Nadal',
                     marker=dict(color='rgba(250, 100, 45, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][11])
    trace13 = go.Bar(x=[2014],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][12])
    trace14 = go.Bar(x=[2015],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][13])
    trace15 = go.Bar(x=[2016],
                     y=[1],
                     name='Murray',
                     marker=dict(color='rgba(250, 174, 255, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][14])
    trace16 = go.Bar(x=[2017],
                     y=[1],
                     name='Federer',
                     marker=dict(color='rgba(150, 85, 255, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][15])
    trace17 = go.Bar(x=[2018],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][16])
    trace18 = go.Bar(x=[2019],
                     y=[1],
                     name='Nadal',
                     marker=dict(color='rgba(250, 100, 45, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][17])
    trace19 = go.Bar(x=[2020],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][18])
    trace20 = go.Bar(x=[2021],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][19])
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13,
            trace14, trace15, trace16, trace17, trace18, trace19, trace20]
    layout = go.Layout(barmode="group", title='Dominance Timeline')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_timeline_1(timeline):
    trace1 = go.Bar(x=[2002],
                    y=[1],
                    name='Hewitt',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][0])
    trace2 = go.Bar(x=[2003],
                    y=[1],
                    name='Roddick',
                    marker=dict(color='rgba(50, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][1])
    trace3 = go.Bar(x=[2004],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][2])
    trace4 = go.Bar(x=[2005],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][3])
    trace5 = go.Bar(x=[2006],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][4])
    trace6 = go.Bar(x=[2007],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][5])
    trace7 = go.Bar(x=[2008],
                    y=[1],
                    name='Nadal',
                    marker=dict(color='rgba(250, 100, 45, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][6])
    trace8 = go.Bar(x=[2009],
                    y=[1],
                    name='Federer',
                    marker=dict(color='rgba(150, 85, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][7])
    trace9 = go.Bar(x=[2010],
                    y=[1],
                    name='Nadal',
                    marker=dict(color='rgba(250, 100, 45, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=timeline['Best Player'][8])
    trace10 = go.Bar(x=[2011],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][9])
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]
    layout = go.Layout(barmode="group", title='Dominance Timeline First Decade')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_timeline_2(timeline):
    trace11 = go.Bar(x=[2012],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][10])
    trace12 = go.Bar(x=[2013],
                     y=[1],
                     name='Nadal',
                     marker=dict(color='rgba(250, 100, 45, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][11])
    trace13 = go.Bar(x=[2014],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][12])
    trace14 = go.Bar(x=[2015],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][13])
    trace15 = go.Bar(x=[2016],
                     y=[1],
                     name='Murray',
                     marker=dict(color='rgba(250, 174, 255, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][14])
    trace16 = go.Bar(x=[2017],
                     y=[1],
                     name='Federer',
                     marker=dict(color='rgba(150, 85, 255, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][15])
    trace17 = go.Bar(x=[2018],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][16])
    trace18 = go.Bar(x=[2019],
                     y=[1],
                     name='Nadal',
                     marker=dict(color='rgba(250, 100, 45, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][17])
    trace19 = go.Bar(x=[2020],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][18])
    trace20 = go.Bar(x=[2021],
                     y=[1],
                     name='Djokovic',
                     marker=dict(color='rgba(250, 174, 20, 0.5)',
                                 line=dict(color='rgb(0,0,0)', width=1.5)),
                     text=timeline['Best Player'][19])
    data = [trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18, trace19, trace20]
    layout = go.Layout(barmode="group", title='Dominance Timeline Second Decade')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

def graph_grandslam_timeline(GS_timeline):
    trace1 = go.Bar(x=GS_timeline.columns,
                    y=[0, 12, 16, 18, 20],
                    name='Federer',
                    marker=dict(color='rgba(255, 174, 255, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=GS_timeline.index[0])

    trace2 = go.Bar(x=GS_timeline.columns,
                    y=[0, 3, 10, 15, 20],
                    name='Nadal',
                    marker=dict(color='rgba(255, 255, 128, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=GS_timeline.index[1])

    trace3 = go.Bar(x=GS_timeline.columns,
                    y=[0, 0, 4, 12, 20],
                    name='Djokovic',
                    marker=dict(color='rgba(255, 150, 56, 0.5)',
                                line=dict(color='rgb(0,0,0)', width=1.5)),
                    text=GS_timeline.index[2])

    data = [trace1, trace2, trace3]

    layout = go.Layout(barmode="group", title='Grand Slam Timeline')

    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)