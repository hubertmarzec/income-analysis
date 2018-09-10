#
#read csv
#group by account No
#agr by sum
#print output
def path_to_data(csv_path):
	data= read_csv(csv_path, sep=',', decimal='.', index_col=0)
	return data
