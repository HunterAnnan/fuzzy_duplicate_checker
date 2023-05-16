import csv
from thefuzz import fuzz

# Read data from and create lists based on first column for...
# ... a first CSV file
with open("first_filepath_here", "r") as file:
    reader = csv.reader(file)
    next(reader)
    data1 = [row[0] for row in reader]

# ... a second CSV file
with open("second_filepath_here", "r") as file:
    reader = csv.reader(file)
    next(reader)
    data2 = [row[0] for row in reader]

number_of_comparisons = len(data1) * len(data2)

if number_of_comparisons > 1000000:
    response = input(f'The number of comparisons ({number_of_comparisons:,}) exceeds 1,000,000. Do you want to continue? (y/n) ')
    if response.lower() != 'y':
        exit()

# Create a CSV file for results to be stored
with open('output_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['String 1', 'String 2', 'Fuzz Ratio'])

    number_of_matches = 0

    # Check for duplicates between the two lists and write to CSV
    for str1 in data1:
        for str2 in data2:
            ratio = fuzz.ratio(str1, str2)
            if ratio > 80:
                writer.writerow([str1, str2, ratio])
                number_of_matches += 1

print(f"Found {number_of_matches} matches with ratio > 80.")
print(f"{number_of_comparisons} comparisons made.")