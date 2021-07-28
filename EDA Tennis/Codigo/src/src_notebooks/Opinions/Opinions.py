import pandas as pd 
import numpy as np

date = ['May 2, 2019', 'Jun 4 2019', 'Jul 14, 2019', 'Jun 15, 2020', 'Jul 11, 2021']
player_1 = ['Federer (20)', 'Federer (20)', 'Federer (20)', 'Federer (20)', 'Federer (20)']
player_1_votes_pct = [None, '72%', '84.5%', None, '65%']
player_2 = ['Nadal (18)', 'Nadal (18)', 'Nadal (18)', 'Nadal (19)', 'Djokovic (20)' ]
player_2_votes_pct = [None, '20%', '8.7%', None, '18%']
player_3 = ['Djokovic (15)', 'Djokovic (15)', 'Djokovic (16)', 'Djokovic (17)', 'Nadal (20)']
player_3_votes_pct = [None, '8%', '6.9%', None, '17%']
total_votes = [None, 43000, 28514, None, 150193]
article = ['The Greatest Men´s Teenis Players of all time', 'Roger Federer wins public vote for Greatest Of All Time',
          'Roger Federer Voted the Greatest Tennis Player of All Time', 'Revealed: World´s Greatest Tennis Players of All Time',
          'Top 10 Greatest Men´s Tennis Players of All Time']
author = ['Claire Gillepie', 'Benjamin Burguess', 'Jack Kenmare', 'Antonia Maria Markou', 'Bill de Giulio']
web = ['The Delite', 'Give me Sport', 'SportBible', 'Ceoworld Magazine', 'How they play']
url = ['https://www.thedelite.com/the-greatest-mens-tennis-players-of-all-time/25/',
       'https://www.givemesport.com/1480600-roger-federer-wins-public-vote-for-greatest-tennis-player-of-all-time',
       'https://www.sportbible.com/tennis/reactions-news-legends-roger-federer-voted-the-greatest-tennis-player-of-all-time-20190714',
       'https://ceoworld.biz/2020/06/15/revealed-worlds-greatest-tennis-players-of-all-time/',
       'https://howtheyplay.com/individual-sports/Top-10-Greatest-Male-Tennis-Players-of-All-Time']

opinions = pd.DataFrame({'Date': date, 'Nº 1': player_1, 'Votes Pct1': player_1_votes_pct,
                        'Nº 2': player_2, 'Votes Pct2': player_2_votes_pct,
                        'Nº 3': player_3, 'Votes Pct3': player_3_votes_pct,
                        'Votes': total_votes, 'Article': article, 'Author': author,
                        'Web' : web, 'URL': url})

opinions