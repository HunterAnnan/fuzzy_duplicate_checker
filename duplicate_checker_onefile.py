import csv
from thefuzz import fuzz

# Read data from file and create a list based on its first column
with open('filepath_here', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [row[0] for row in reader]
    
#calculate the number of comparisons to make
#(and conditional check with the user to proceed)
number_of_comparisons = (len(data) * len(data) - 1) // 2
    
if number_of_comparisons > 1000000:
    response = input(f'The number of comparisons ({number_of_comparisons:,}) exceeds 1,000,000. Do you want to continue? (y/n) ')
    if response.lower() != 'y':
        exit()

#create a CSV file for results to be stored
with open('output_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['String 1', 'String 2', 'Fuzz Ratio'])

    number_of_matches = 0

# Check for near-duplicates in the list and write to CSV
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            ratio = fuzz.ratio(data[i], data[j])
            if ratio > 80:
                writer.writerow([data[i], data[j], ratio])
                number_of_matches += 1
                
print(f"Found {number_of_matches} matches with ratio > 80.")
print(f"{number_of_comparisons} comparisons made.")