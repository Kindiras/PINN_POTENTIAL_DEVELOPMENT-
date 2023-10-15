import csv

 # Specify the input .dat file and output CSV file
 input_file = "RMSE_vs_cluster.dat"
 output_file = "outputn.csv"

 # Read data from the .dat file and write it to the CSV file
 with open(input_file, "r") as dat_file, open(output_file, "w", newline="") as csv_file:
     # Specify the delimiter used in your .dat file (e.g., space, tab, comma, etc.)
     # For example, if the values in your .dat file are separated by spaces:
     delimiter = " "

     # Create a CSV writer
     csv_writer = csv.writer(csv_file)

     # Read each line from the .dat file and write it to the CSV file
     for line in dat_file:
         # Split the line into values based on the delimiter
         values = line.strip().split(delimiter)
         # Write the values to the CSV file
         csv_writer.writerow(values)

 print(f"Data from {input_file} has been converted and written to {output_file}.")