import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Get our US State data supplied by The New York Times.
state_data =pd.read_csv('~/Code/covid-19-data/us-states.csv')
#print(state_data.loc[state_data['state']=='Florida'])