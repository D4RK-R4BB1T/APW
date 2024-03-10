import requests

def generate_memberlist_links(base_url, total_pages):
    # Page one link without queries
    page_one_link = f"{base_url}/memberlist.php"
    print(page_one_link)

    # Generate links with queries for page 2 and beyond
    for page_number in range(2, total_pages + 1):
        page_link = f"{base_url}/memberlist.php?sort=regdate&order=ascending&perpage=20&page={page_number}"
        print(page_link)

    # Export links to a txt file
    with open("memberlist_links.txt", "w") as file:
        file.write(page_one_link + "\n")
        for page_number in range(2, total_pages + 1):
            page_link = f"{base_url}/memberlist.php?sort=regdate&order=ascending&perpage=20&page={page_number}"
            file.write(page_link + "\n")

if __name__ == "__main__":
    # Set console text color to lime green
    print("\033[92m")

    # Get user input for base URL and total pages
    base_url = input("Enter the base URL (e.g., http://example.com): ")
    total_pages = int(input("Enter the total number of pages to generate: "))

    # Generate and print links
    generate_memberlist_links(base_url, total_pages)

    # Reset console text color
    print("\033[0m")
