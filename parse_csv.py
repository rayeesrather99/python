import csv

# This program reads data from 'students.csv' and writes it to 'new_students.csv'
# using '-' as the delimiter.

# Open the original CSV file in read mode
with open('students.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Open the new file in write mode
    with open('new_students.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        # Read each row from the original file and write it to the new file
        for row in csv_reader:
            csv_writer.writerow(row)
