# Import libraries
import requests
from bs4 import BeautifulSoup
import os



# URL from which pdfs to be downloaded
url = "https://www.cs.cmu.edu/afs/cs/academic/class/15210-s14/www/lectures/"

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

i = 0

# From all links check for pdf link and
# if present download file
for link in links:
    if '.pdf' in link.get('href', []):
        i += 1
        print("Downloading file: ", i)
	    # Get response object for link
        lnkhref = link.get('href')
        pdflink = f"{url}{lnkhref}"
        response = requests.get(pdflink)
        # Write content in pdf file
        # tempTuple = os.path.splitext(lnkhref)

        dir_path = os.path.dirname(os.path.realpath(__file__))

        pdf = open(f"{dir_path}\graph\pdfs\{lnkhref}", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")
        
        
       

print("All PDF files downloaded")

		