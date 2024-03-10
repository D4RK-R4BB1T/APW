def remove_after_slash(input_string):
    # Find the index of the first '/'
    index = input_string.find('/')
    
    # If '/' is found, return the string up to that point, otherwise, return the original string
    return input_string[:index] if index != -1 else input_string

def process_file(file_path):
    with open(file_path, 'r') as file:
        input_strings = [line.strip() for line in file.readlines()]

    cleaned_strings = [remove_after_slash(string) for string in input_strings]

    with open('cleaned_output.txt', 'w') as output_file:
        output_file.write('\n'.join(cleaned_strings))

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")

    try:
        process_file(file_path)
        print("Processing complete. Cleaned strings saved to 'cleaned_output.txt'.")
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
