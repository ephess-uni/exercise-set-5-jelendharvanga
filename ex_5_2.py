import numpy as np

# Generate some random data
data = np.random.rand(100)

# TODO: Modify the data to have a mean of 0
data -= np.mean(data)

# TODO: Modify the zero mean data to have a standard deviation of 1
data /= np.std(data)

# Save the processed data to a variable called 'processed'
processed = data

# Save the processed data to a file
np.savetxt('processed_data.txt', processed)

# Load the saved data from the file
loaded_data = np.loadtxt('processed_data.txt')

# Print the loaded data
print(loaded_data)
