import csv
with open('filmy.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)  # Create DictReader

    data_list = []  # List to store dictionaries
    for row in csv_reader:
        data_list.append(row)

for data in data_list:
    print(data)