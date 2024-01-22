import requests
from bs4 import BeautifulSoup

# URL of Wikipedia main page
url = ""

# Send an HTTP request to the URL
response = requests.get("")

# Check if the request was successful
if response.status_code == 'ENTER SUCCESSFUL STATUS CODE':
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the div (by id) containing the description of the featured article
    featured_div = soup.find('div', {'id': ''})
    
    # Only get the text, not the image
    featured_text = ""

    # Print the result
    print("Today's Featured Article Description:")
    print(featured_text)