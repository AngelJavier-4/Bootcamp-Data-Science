import pandas as pd
import numpy as np

#Lectura de los csv
BPfacedpermatch = pd.read_csv('StatisticsLeaders_BPfacedpermatch.csv')
BPsavedpct = pd.read_csv('StatisticsLeaders_BPsavedpct.csv')
firstservepctwon = pd.read_csv('StatisticsLeaders_firstservepctwon.csv')
secondservepctwon = pd.read_csv('StatisticsLeaders_secondservepctwon.csv')
firstservepct = pd.read_csv('StatisticsLeaders_firstservepct.csv')

#Retocada la tabla de BP faced per match
BP = BPfacedpermatch.copy()
BP.rename(columns = {'value':'BP Faced per Match'}, inplace = True)
del BP['rank']
del BP['country_name']
del BP['active']
BP.head()

#Retocada la tabla de BP saved percentage
BP1 = BPsavedpct.copy()
BP1.rename(columns = {'value':'BP saved %'}, inplace = True)
del BP1['rank']
del BP1['country_name']
del BP1['active']
BP1.head()

#Retocada la tabla de Return 1st won percentage
BP2 = firstservepctwon.copy()
BP2.rename(columns = {'value': '1st serve won %'}, inplace = True)
del BP2['rank']
del BP2['country_name']
del BP2['active']
BP2.head()

#Retocada la tabla de Return 2nd won percentage
BP3 = secondservepctwon.copy()
BP3.rename(columns = {'value':'2nd serve won %'}, inplace = True)
del BP3['rank']
del BP3['country_name']
del BP3['active']
BP3.head()

#Retocada la tabla de serve percentage
BP4 = firstservepct.copy()
BP4.rename(columns = {'value':'1st Serve %'}, inplace = True)
del BP4['rank']
del BP4['country_name']
del BP4['active']
BP4.head()

#Concatenado de todas las tablas
serve = [df.set_index(['name' , 'country_id']) for df in [BP4, BP2, BP3, BP, BP1]]

serve = pd.concat(serve, axis=1).reset_index()
serve

#Mascara
big3serve = serve[(serve['name'] == 'Roger Federer') | (serve['name'] == 'Rafael Nadal') | (serve['name'] == 'Novak Djokovic')]
big3serve

