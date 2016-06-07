import boto
import csv
import random
from boto import dynamodb2
from boto.dynamodb2.exceptions import ItemNotFound
from boto.dynamodb2.table import Table
from boto.dynamodb.condition import LE, EQ, GE, BETWEEN

def cc_prediction(From_user,TO_USER):
	dynamodb_conn = boto.dynamodb2.connect_to_region('us-west-2')
	dynamodb_table = Table('Enron_Data',connection=dynamodb_conn)
	print From_user
	print TO_USER
	to_user_list = dynamodb_table.query_2(From__eq =From_user,To_List__eq =TO_USER)
	no_of_cc = 2
	cc_list = []

	print to_user_list.__sizeof__()
	for user in to_user_list:
		print "In"
		cc_list = user['CC']
	predicted_list = []
	if len(cc_list) > 0:
		predicted_list = random.sample(cc_list,no_of_cc)
	return predicted_list



