#! python3.7
# google_Search.py - Opens several Google seach results.

import requests, webbrowser, bs4, sys, pyperclip #argumentOrClipboard

# address = argumentOrClipboard: durch das einfügen von dem Modul sollen die nächsten 4 Zeilen Code eingespart werden

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print("Google...") # Display text while downloading the google page
res = requests.get("https://google.com/search?q=" + address)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
    print("Fertig")
