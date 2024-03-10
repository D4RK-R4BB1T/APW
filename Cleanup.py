import os
import re
import csv
from urllib.parse import urlparse

def remove_blacklisted_strings(file_path, blacklist):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f]

    cleaned_lines = []

    for line in lines:
        # Check if any blacklisted term is present in the line
        if not any(item.lower() in line.lower() for item in blacklist):
            cleaned_lines.append(line)
        else:
            # If a blacklisted term is found, remove the entire line
            cleaned_lines.extend([l for l in re.split(r'\s+', line) if not any(item.lower() in l.lower() for item in blacklist)])

    with open(file_path, 'w') as f:
        f.write('\n'.join(cleaned_lines))

def parse_data_by_extensions(file_path, extensions, output_file):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f]

    parsed_lines = [line for line in lines if any(ext.lower() in line.lower() for ext in extensions)]

    with open(output_file, 'a') as f:
        f.write('\n'.join(parsed_lines) + '\n')

def remove_characters(file_path, characters, output_file, direction):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f]

    if direction == 'before':
        cleaned_lines = [re.sub(rf'.*{re.escape(characters)}', '', line) for line in lines]
    elif direction == 'after':
        cleaned_lines = [re.sub(rf'{re.escape(characters)}.*', '', line) for line in lines]
    else:
        cleaned_lines = [line.replace(characters, '') for line in lines]

    with open(output_file, 'w') as f:
        f.write('\n'.join(cleaned_lines))

def remove_duplicates(input_directory, output_file):
    unique_strings = set()

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f]
                unique_strings.update(lines)

    with open(output_file, 'w') as f:
        f.write('\n'.join(unique_strings))

def dump_to_master_list(input_directory, output_file, output_format):
    all_strings = []

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f]
                all_strings.extend(lines)

    if output_format == 'csv':
        with open(output_file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Strings'])
            csvwriter.writerows([[string] for string in all_strings])
    else:
        with open(output_file, 'w') as f:
            f.write('\n'.join(all_strings))

def cleanup_script():
    print("Options:")
    print("1. Remove Blacklisted Strings")
    print("2. Parse Data by Extensions")
    print("3. Remove Characters")
    print("4. Remove Duplicates")
    print("5. Dump to Master List")

    choice = input("Enter the number of the operation you want to perform: ")

    directory = input("Enter the directory to process: ")

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    if choice == '1':
        blacklist_file = input("Enter the path to the blacklist file: ")
        if not os.path.exists(blacklist_file):
            print(f"Error: Blacklist file '{blacklist_file}' does not exist.")
            return
        with open(blacklist_file, 'r') as f:
            blacklist = [line.strip() for line in f.readlines()]
        for root, dirs, files in os.walk(directory, topdown=True):
            for file in files:
                file_path = os.path.join(root, file)
                remove_blacklisted_strings(file_path, blacklist)
    elif choice == '2':
        extensions_file = input("Enter the path to the extensions file: ")
        if not os.path.exists(extensions_file):
            print(f"Error: Extensions file '{extensions_file}' does not exist.")
            return
        with open(extensions_file, 'r') as f:
            extensions = [line.strip() for line in f.readlines()]
        for root, dirs, files in os.walk(directory, topdown=True):
            for file in files:
                file_path = os.path.join(root, file)
                parse_data_by_extensions(file_path, extensions, 'T2R.txt')
    elif choice == '3':
        characters_file = input("Enter the path to the characters file: ")
        if not os.path.exists(characters_file):
            print(f"Error: Characters file '{characters_file}' does not exist.")
            return
        with open(characters_file, 'r') as f:
            characters = f.read().strip()
        direction = input("Enter 'before' to remove everything before characters, 'after' to remove everything after characters, or 'both' to remove characters: ")
        for root, dirs, files in os.walk(directory, topdown=True):
            for file in files:
                file_path = os.path.join(root, file)
                remove_characters(file_path, characters, 'RC.txt', direction)
    elif choice == '4':
        remove_duplicates(directory, 'output/unique_strings.txt')
    elif choice == '5':
        output_format = input("Enter 'txt' or 'csv' for output format: ")
        dump_to_master_list(directory, 'output/master_list.' + output_format, output_format)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    cleanup_script()
