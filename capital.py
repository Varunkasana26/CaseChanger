# Function to convert lowercase to uppercase in a file
def convert_to_uppercase(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Convert content to uppercase
        upper_content = content.upper()
        
        # Write the converted content to the output file
        with open(output_file, 'w') as file:
            file.write(upper_content)
        
        print(f"Conversion successful! Check the output file: {output_file}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "E:\\Python project\\captialletter\\input.txt"  # Replace with your input file name
output_file = "E:\\Python project\\captialletter\\output.txt"  # Replace with your desired output file name
convert_to_uppercase(input_file, output_file)