import requests
from bs4 import BeautifulSoup
import csv

keyword=str(input("Scrape Top 10 Google Search Results ===> "))

google_url = f"https://www.google.com/search?q= + {keyword}"

response = requests.get(google_url)
soup = BeautifulSoup(response.text, "html.parser")

result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})

links = []
titles = []
descriptions = []
for r in result_div:
    # Checks if each element is present, else, raise exception
    try:
        link = r.find('a', href = True)
        title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
        description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
        
        # Check to make sure everything is present before appending
        if link != '' and title != '' and description != '': 
            links.append(link['href'].split("?q=")[1])
            titles.append(title)
            descriptions.append(description)
    # Next loop if one element is not present
    except:
        continue

# Save Results into.CSV file following link, title and description of result.
csv_file=open("search_history.csv","w", encoding="utf-8")
csv_write=csv.writer(csv_file)

for li, ti, desc in zip(links, titles, descriptions):
  csv_write.writerow([li, ti, desc])

csv_file.close()


