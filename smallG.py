# Calculating the Acceleration due to Gravity of all the planets in the Solar System (+ Pluto!)
import numpy as np
import pandas as pd
import pickle
Solar_Data= pd.read_pickle('Solar.pickle')
Solar_Data['V due to Grvty']=(6.67*(10**-11)*Solar_Data['Mean_Mass'])/(Solar_Data['Radius']*1000)**2
print('The Acceleration due to Gravity data is\n',Solar_Data)
