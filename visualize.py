import pandas as pd 
import matplotlib.pyplot as plt 
import sys

'''
Script to visualize sensor data recorded from mobile in 2D Graph plots
Data needed for running the script
1. CSV file containing recorded sensor data (App used: Physics Toolbox:Android)
2. Name of the data to be visualized (e.g.: Roll, Pitch)

example usage:
Assuming filename to be 'data.csv' and data to be plotted is 'Row'
	python visualize.py Row
'''

def main():
	# String for displaying errors
	error_message = "Please specify atleast 3 arguments\nExample usage:\n\tpython visualize.py file_name.csv column_name_1 column_name_2"

	# Return if there are no arguments
	if (len(sys.argv)<3):
		print (error_message)

	# Get the csv file through command line
	data = pd.read_csv(sys.argv[1])
	# print (data['time'])

	# Plot each column
	for i in range(2, len(sys.argv)):
		plt.subplot(len(sys.argv)-1, 1, i-1)
		plt.plot(data['time'], data[sys.argv[i]])
		plt.ylabel(sys.argv[i])

	plt.subplot(len(sys.argv)-1, 1, i)

	plt.scatter(data['gFx'], data['gFy'])

	plt.show()



if __name__ == '__main__':
	main()