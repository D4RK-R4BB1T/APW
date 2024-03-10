import os
import argparse

def process_files(directory, string_to_remove):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
            content = content.replace(string_to_remove, '\n')
            with open(file_path, 'w') as file:
                file.write(content)

def main():
    parser = argparse.ArgumentParser(description="Process files in a directory")
    parser.add_argument("directory", help="Path to the directory containing files")
    parser.add_argument("-s", "--string", help="String to be removed and replaced with a newline character")

    args = parser.parse_args()

    if not args.string:
        print("Error: Please specify the string to be removed using the -s argument.")
        return

    process_files(args.directory, args.string)
    print("Files processed successfully.")

if __name__ == "__main__":
    main()
