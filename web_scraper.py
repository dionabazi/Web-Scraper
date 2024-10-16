import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Adjust the selector to match the website's structure
        titles = soup.find_all('h2')  # Assuming article titles are in <h2> tags

        print(f"Found {len(titles)} titles:")
        for i, title in enumerate(titles, start=1):
            print(f"{i}: {title.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the website to scrape: ")
    scrape_titles(url)
