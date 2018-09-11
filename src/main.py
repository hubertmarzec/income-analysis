from app import path_to_data
from app import pick_wanted_cols

data = path_to_data('../data/Historia_Rachunku_180206_211715.csv')
#print(data)

data_in_cols = pick_wanted_cols(data,7,8,4)
#print(data_in_cols)


data=data_in_cols
# for group, items in itertools.groupby(list(data)):
#   print (group, list(items))

print(data)

data_nn=list(zip(data[0], data[1], data[2]))
print(data_nn)



data_nn[2] = [float(i) for i in data_nn[1]]



for number,name, amount in data_nn[1:]:
	print(number,name, sum(amount))

# for entry in list(data):
#   group=entry[0]

#   for group, entry[2] in data.groupby(data):
#     print(group, list(items))
