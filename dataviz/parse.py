import csv

MY_FILE = '...'

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

def main():
	new_data = parse(MY_FILE, ',')
	print (new_data)

if __name__ == '__main__':
	main()