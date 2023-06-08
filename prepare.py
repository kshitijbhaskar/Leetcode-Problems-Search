# Open the file in read mode
file = open('index.txt', 'r')

# Create an empty dictionary
data = {}
i=0
# Iterate over each line in the file
for line in file:
    # Split the line into key-value pairs
    key, value = line.strip().split('.')
    i=i+1
    # Store the key-value pair in the dictionary
    data[i] = value
# Close the file
file.close()

# Print the dictionary
print(data)
