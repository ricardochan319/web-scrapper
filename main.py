import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Fetch the web page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the HTML
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return links
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    url = input("Enter the URL to scrape: ")
    scraped_data = scrape_website(url)

    if isinstance(scraped_data, list):
        print("Scraped data:")
        for link in scraped_data:
            print(link)
    else:
        print(scraped_data)

if __name__ == '__main__':
    main()
