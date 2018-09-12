from app import path_to_data
from app import pick_wanted_cols
from app import path_to_dictionary
from app import data_summary

data= path_to_dictionary('../data/Historia_Rachunku_180206_211715.csv')

print(data)

data_s = data_summary(data)

print(data_s)


