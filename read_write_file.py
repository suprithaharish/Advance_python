
# to read file  
file_path = r"C:\Users\Janavi\OneDrive\Desktop\Adv_py\input.txt"

with open(file_path, "r") as file:
    data = file.read()

print(data)

#And to write that content into another file:
file_path = r"C:\Users\Janavi\OneDrive\Desktop\Adv_py\input.txt"
output_path = r"C:\Users\Janavi\OneDrive\Desktop\Adv_py\output.txt"

with open(file_path, "r") as file:
    data = file.read()

with open(output_path, "w") as file:
    file.write(data)

print("File copied successfully!")





"""
# Ask the user for the input file path
file_path = input("Enter the path of the input file: ")

# Read the file
with open(file_path, "r") as file:
    data = file.read()

print("\nFile content:")
print(data)

# Ask the user for the output file path
output_path = input("\nEnter the path of the output file: ")

# Write the content into the output file
with open(output_path, "w") as file:
    file.write(data)

print("File copied successfully!")
"""