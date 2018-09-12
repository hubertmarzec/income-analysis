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

def path_to_dictionary(csv_path):

  import csv

  with open(csv_path, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    
    data_dict = {rows[7]:[rows[8], rows[4]] for rows in reader}


  return data_dict

def data_summary(data):

  key_to_remove='Rachunek nadawcy/odbiorcy'
  del data[key_to_remove]
  #Removes description key for keys in data

  for key, val in data.items():
    key.format("'","")
    (val[1]).format("'","")
    summary=(
      key.count(key),
      val[0],
      float(val[1]).agr(sum)
      )
  return summary



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
