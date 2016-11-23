import csv
from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = '/home/local/py3eg/dataviz/sample_sfpd_incident_all.csv'

def parse(raw_file, delimiter):
	"""Parse raw CSV file """

	# Open csv file
	opened_file = open(raw_file)

	# Read csv file
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	#An entry list
	parsed_data=[]

	#Skip first line of file (headers)
	fields = csv_data.next()

	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close csv file
	opened_file.close()
	# Built data structure to return parsed data
	return parsed_data

def visualize_days():
	# grab our parsed data that we parsed earlier
	data_file = parse(MY_FILE, ',')
	
	# make a new variable, 'counter', from iterating through each
	# line of data in the parsed data, and count how many incidents
	# happen on each day of the week
	counter = Counter(item["DayOfWeek"] for item in data_file)

	# separate the x-axis data (the days of the week) from the
	# 'counter' variable from the y-axis data (the number of
	# incidents for each day)
	data_list = [
				counter["Monday"],
				counter["Tuesday"],
				counter["Wednesday"],
				counter["Thursday"],
				counter["Friday"],
				counter["Saturday"],
				counter["Sunday"]
				]
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

	# with that y-axis data, assign it to a matplotlib plot instance
	plt.plot(data_list)
	plt.xticks(range(len(day_tuple)), day_tuple)

	# save the plot!
	plt.savefig('days.png')

	# close plot file
	plt.clf()

if __name__ == '__main__':
	visualize_days()