with open("scrap.txt", "rb") as file:
    scrap_data = file.read()

import csv

from bs4 import BeautifulSoup
from google_images_download import google_images_download

soup = BeautifulSoup(scrap_data, 'html.parser')
memes = []

tabledata = soup.find_all("td")

for data in tabledata:
    if data.h2 and data.h2.get_text().isascii():
        memes.append(
            (data.h2.get_text(strip=True).split('/')[0].replace(",|:",""), data.a['href'])
        )

with open('meme_list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for name, url in memes:
        writer.writerow([name, url])
meme_names = [name for name, url in memes]

for meme in meme_names:

    response = google_images_download.googleimagesdownload()   #class instantiation
    arguments = {"keywords":meme,
                 "limit":1,
                 "print_urls":False,
                 "sk":"meme"}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)   #printing absolute paths of the downloaded images


print(meme_names)
#print(soup.prettify())