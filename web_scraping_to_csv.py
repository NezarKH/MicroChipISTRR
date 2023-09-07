import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website
url = 'https://forum.microchip.com/'

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all text in the webpage
texts = soup.stripped_strings

# Create a list to store all words
words_list = []

# Loop through the texts to split them into words
for text in texts:
    words = text.split()
    words_list.extend(words)

# Remove duplicates
unique_words = list(set(words_list))

# Save the words to a CSV file
with open('words.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Words'])
    for word in unique_words:
        writer.writerow([word])

print('CSV file has been created.')
