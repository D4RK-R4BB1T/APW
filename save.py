import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

def read_links_from_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def normalize_url(url):
    # Add 'http://' if no scheme provided
    if not urlparse(url).scheme:
        url = 'http://' + url
    return urlunparse(urlparse(url)._replace(path='', params='', query='', fragment=''))

def download_html_documents(links, save_directory):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for index, link in enumerate(links, start=1):
        full_link = normalize_url(link)
        response = requests.get(full_link)
        if response.status_code == 200:
            html_content = response.text
            file_path = os.path.join(save_directory, f"page_{index}.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(html_content)
            print(f"Page {index} downloaded successfully to {file_path}.")
        else:
            print(f"Failed to download page {index}. Status code: {response.status_code}")

def parse_html_documents():
    # Add your HTML parsing logic here using BeautifulSoup
    pass

if __name__ == "__main__":
    # Set console text color to lime green
    print("\033[92m")

    # Get user input for the file path containing links
    file_path = input("Enter the file path containing links: ")

    # Get user input for the directory to save HTML files
    save_directory = input("Enter the directory to save HTML files: ")

    # Read links from file
    memberlist_links = read_links_from_file(file_path)

    # Download HTML documents
    download_html_documents(memberlist_links, save_directory)

    # Reset console text color
    print("\033[0m")
