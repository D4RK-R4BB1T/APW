import os
import re

def extract_user_info(html_file):
    with open(html_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Use regular expression to find patterns like <a href="...uid=1">MattH</a>
    pattern = r'<a href=".*?uid=(\d+)">(.*?)</a>'
    matches = re.findall(pattern, content)

    user_info_list = [f"{uid}:{display_name}" for uid, display_name in matches]
    return user_info_list

def extract_and_save_user_info(html_folder, master_file):
    with open(master_file, "w", encoding="utf-8") as master:
        for filename in os.listdir(html_folder):
            if filename.endswith(".html"):
                html_file_path = os.path.join(html_folder, filename)
                user_info_list = extract_user_info(html_file_path)
                if user_info_list:
                    master.write("\n".join(user_info_list) + "\n")

if __name__ == "__main__":
    # Get user input for the HTML folder and master file
    html_folder = input("Enter the directory containing HTML files: ")
    master_file = input("Enter the path for the master text file: ")

    # Ensure the master file directory exists
    master_dir = os.path.dirname(master_file)
    if not os.path.exists(master_dir):
        os.makedirs(master_dir)

    # Extract and save user info from HTML files
    extract_and_save_user_info(html_folder, master_file)

    print("Extraction completed. Check the master text file for results.")
