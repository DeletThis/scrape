from scrape import read_scraped_memes

import csv
import sys
from google_images_download import google_images_download

LIMIT = 50
PRINT_URLS = True

def download_meme(meme: str):
    name = meme.name
    folder = meme.url.split('/')[2]
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": name,
                 "limit": LIMIT,
                 "image_directory": folder,
                 "prefix": folder,
                 "print_urls": PRINT_URLS,
                 "sk": "meme"
                 }
    paths = response.download(arguments)
    print(folder)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage: python download.py [path_to_scraped_memes]')
    else:
        memes = read_scraped_memes(sys.argv[1])
        for meme in memes:
            download_meme(meme)