import webbrowser, sys
#import pyperclip #thirdparty
#opens webbrowser
webbrowser.open('http://google.com')


sys.argv # [mapit.py, '870', 'valencia', 'St.']
#check if command line arguments were passed 
if len(sys.argv) > 1:
    #['mapit.py', '870', 'valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
#else:
    #address = pyperclip.paste()

#https://www.google.com/maps/place/<ADDRESS>
googlemaps = 'https://www.google.com/maps/place/'
webbrowser.open(googlemaps + address )






# Download Files from the WEB - Dont have to worry about:
# Network errors - Connection Problems - Data Compression.

import requests # thirdparty  `pip install requests`
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code # use try catch

len(res.text)

res.text[:500]
res.raise_for_status() # raises an exection if something happends 

# to save you need open the file first  - to open it you need to pass 'wb' write binary command - for unicode encoding
playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000): # this reads the response by chunks (bytes data type) at a time
    playFile.write(chunk)








# Parsing HTML with the beautiful Soup Module beautifulsoup4
import bs4
import requests
res = requests.get('https://www.google.com')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elem = soup.select('#lga')
elem[0].text.strip() #strip removes new lines



# Example:
import bs4, requests
def getAmazonPrices(productUrl)
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#some-id')
    return elems[0].text.strip()


price = getAmazonPrices('https://amazon.com/fakeproduct')
print('The price is ' + price)





