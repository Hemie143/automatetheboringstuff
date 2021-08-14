#! python3
# downloadXkcd.py - downloads evert single XKCD comic

import requests
import os
import bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the page
    print(f'Downloading page {url}')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = f'https:{comicElem[0].get("src")}'

    # Download the image
    print(f'Downloading image {comicUrl}')
    res = requests.get(comicUrl)
    res.raise_for_status()

    # Save the image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = f'https://xkcd.com{prevLink.get("href")}'
    
print('Done.')