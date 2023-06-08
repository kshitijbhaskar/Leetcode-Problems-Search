import os

# Define the path to the index file and the q-data folder
index_file = 'index.txt'
q_data_folder = 'q-data'

# Read the index file with latin-1 encoding
with open(index_file, 'r', encoding='latin-1') as file:
    index_lines = file.readlines()

number=0

# Process each line in the index file
processed_lines = []
for line in index_lines:
    # Extract the question number and description
    numbers, question = line.strip().split('.', 1)
    question = question.strip()
    number=number+1
    # Find the corresponding folder path and description file
    folder_path = os.path.join(q_data_folder, str(number))
    description_file = os.path.join(folder_path, f"{number}.txt")

    # Read the description from the file in the folder until "Example" is encountered
    with open(description_file, 'r', encoding='latin-1') as file:
        description_lines = []
        for desc_line in file:
            desc_line = desc_line.strip()
            if desc_line.lower() == 'example':
                break
            description_lines.append(desc_line)

        description = ' '.join(description_lines)

    # Append the description to the line, removing the number and dot
    processed_line = f'{question} {description}\n'
    processed_lines.append(processed_line)

# Write the processed lines to a new file with latin-1 encoding
output_file = 'output.txt'
with open(output_file, 'w', encoding='latin-1') as file:
    file.writelines(processed_lines)

print(f"Processed lines have been written to {output_file}.")
