#
#read csv
#group by account No
#agr by sum
#print output
def path_to_data(csv_path):
  import csv
  with open (csv_path, 'r' ) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    data=[]
    for row in reader:
      data.append(row)
  return data

  # with open (csv_path , 'rb') as csvfile:
  #   reader = csv.reader(csvfile, delimiter = ',')
  #   # for row in reader:
  #   #     row = csvfile.readline()
  #   #     data=data.append(row)
  #   data=[]

  #   for row in reader:
  #     data = data.append(row)



def pick_wanted_cols(data, index_for_account, index_for_name, index_for_amount):
  data_a=[]
  data_n=[]
  data_am=[]

  
  for entry in list(data):
    
    data_a.append(entry[7])
    data_n.append(entry[8])
    data_am.append(entry[4])
  n_data=[data_a,data_n,data_am]
  
  return n_data






# def group_by_account_no(data):
  
#   data.group_by(data['account_no'])

#   return grouped_data
# for entry in list(data):
#   group=entry[0]

#   for group, items in itertools.groupby(list(data)):
#     print (group, list(items))



def sum_amount(data):


  data = data.sum(data['amount'])

  return summed_amount_data
