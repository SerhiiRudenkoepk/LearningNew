import csv

weather_list = []

with open('weather_data.csv') as data_file:
    csv_reader = csv.reader(data_file) # reads the file
    for row in csv_reader:
        weather_list.append(row) 

print(weather_list)