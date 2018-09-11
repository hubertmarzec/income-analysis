from app import payment_summary
from util import d

data = payment_summary('../data/Historia_Rachunku_180206_211715.csv')
d(data)
d('--> number of records {0}'.format(len(data)))
