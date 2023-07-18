import argparse
import numpy as np

def process_data(infile, outfile):
    # Load the data from the input file
    data = np.loadtxt(infile)

    # Modify the input data to have a mean of 0
    mean_centered = data - np.mean(data)

    # Modify the mean-centered data to have a standard deviation of 1
    processed = mean_centered / np.std(mean_centered)

    # Save the processed data to the output file
    np.savetxt(outfile, processed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This program applies a standard scale transform to the data in infile and writes it to outfile.')
    parser.add_argument('infile', help='Input filename for the data file')
    parser.add_argument('outfile', help='Output filename')
    args = parser.parse_args()

    process_data(args.infile, args.outfile)
