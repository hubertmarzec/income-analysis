
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

# return list of dicts with keys: account, name, amount_sum
def calculate_sum(data):
  result = []
  return result;

def group_by_account(data):
  grouped = {}
  for row in data:
    if row['account'] in grouped:
      grouped[row['account']]['amount_sum'] = grouped[row['account']]['amount_sum'] + row['amount']
    else:
      grouped[row['account']] = {'account' : row['account'], 'name' : row['name'], 'amount_sum' : row['amount']}
  return grouped;

