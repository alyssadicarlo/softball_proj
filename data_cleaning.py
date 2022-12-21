import pandas as pd
import numpy as np

players_df = pd.read_csv('softball_data.csv')
all_americans_df = pd.read_csv('all_americans.csv')

all_americans = [str(player) for player in all_americans_df.player]

players_df['all_american'] = [True if x in all_americans else False for x in players_df.player]

players_df.to_csv('final.csv')