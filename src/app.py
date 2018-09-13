
# main function
def payment_summary(csv_path):
  prepared_data = parse_csv(csv_path)
  grouped = group_by_account(prepared_data)
  data = list(grouped.values())
  return data

# return list of dicts with keys: account, amount, name
def parse_csv(csv_path):
  import csv
  data=[]
  with open (csv_path, 'r' ) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader) # skip first line (header)
    for row in reader:
      data.append({'account' : row[7], 'amount' : float(row[4]), 'name': row[8]})
  return data

# <<<<<<< HEAD
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
  data_dict=[]
  with open(csv_path, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
      data_entry = {'account_No':row[7],'account_Holder':row[8],'amount':float(row[4])}  
      data_dict.append(data_entry)

  return data_dict

def data_summary(data):
  grouped_by_account={}
  for row in data:
    if row['account_No'] not in grouped_by_account:
      grouped_by_account[row['account_No']]={'account_No':row['account_No'],
      'account_Holder':row['account_Holder'],'Total_amount':row['amount']}
    else:
      grouped_by_account[row['account_No']]['Total_amount']=grouped_by_account[row['account_No']]['Total_amount']+row['amount']
  
  return grouped_by_account



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



# def sum_amount(data):


#   data = data.sum(data['amount'])
# =======
# def group_by_account(data):
#   grouped = {}
#   for row in data:
#     if row['account'] in grouped:
#       grouped[row['account']]['amount_sum'] = grouped[row['account']]['amount_sum'] + row['amount']
#     else:
#       grouped[row['account']] = {'account' : row['account'], 'name' : row['name'], 'amount_sum' : row['amount']}
#   return grouped;
# >>>>>>> 08d6dccdac85ee090c18ae820e483f3d7b81a615

