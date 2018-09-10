#
#read csv
#group by account No
#agr by sum
#print output
def path_to_data(csv_path):
  import csv
  with open (csv_path) as csvfile:
   data= csv.reader(csvfile, delimiter=",")
   
  result=[]  
  return result

def pick_wanted_cols(data, index_for_account, index_for_name, index_for_amount):

  data[index_for_account]='account_no'
  data[index_for_name]='name'
  data[index_for_amount]='amount'

  data=data[:,['account_no','name','amount']].index_col=0
  data=data.values

  return data

def group_by_account_no(data):
  
  data.group_by(data['account_no'])

  return grouped_data


def sum_amount(data):

  data = data.sum(data['amount'])

  return summed_amount_data
