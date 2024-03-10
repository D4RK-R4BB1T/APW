import os
import requests
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

    # Use a session to handle cookies and headers
    with requests.Session() as session:
        for index, link in enumerate(links, start=1):
            full_link = normalize_url(link)
            try:
                response = session.get(full_link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
                response.raise_for_status()  # Raise HTTPError for bad responses
                html_content = response.text
                file_path = os.path.join(save_directory, f"page_{index}.html")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(html_content)
                print(f"Page {index} downloaded successfully to {file_path}.")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download page {index}. Error: {e}")

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
