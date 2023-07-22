import numpy as np
from pathlib import Path

# Get the root directory of the repository
root_directory = Path.cwd().parent

# Input and output file paths
infile = root_directory / 'data' / 'ex_5_4-data.csv'
outfile = root_directory / 'outputs' / 'ex_5_4-processed.csv'

# Load the array from the input file
data = np.loadtxt(infile)

# Set negative elements to 0
processed = np.where(data < 0, 0, data)

# Save the processed array to the output file
np.savetxt(outfile, processed, delimiter=',')

print("Processed array saved to:", outfile)
