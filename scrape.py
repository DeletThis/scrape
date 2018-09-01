from meme import Meme
import csv
import re
import time
import sys
from bs4 import BeautifulSoup

MANUAL = True
URL = "https://knowyourmeme.com/memes/popular"

def read_html(path: str) -> bytes:
    """Reads an html file"""
    with open(path, 'rb') as file:
        return file.read()

def get_soup(html: bytes) -> BeautifulSoup:
    """Returns BeautifulSoup object from a html file."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def scrape_memes(soup: BeautifulSoup) -> list:
    """Scrapes the html to get a list of memes."""
    memes = []
    soup_meme = soup.select('td[class*="entry"]')
    print(soup_meme)
    for item in soup_meme:
        meme = Meme(item.h2.get_text(strip=True), item.a['href'])
        while MANUAL and not meme.is_alphanumspace():
            meme.name = input(f'Replace {meme.name}:')

        memes.append(meme)
    return memes

def write_scraped_memes(memes: list):
    """Writes the memes to a csv"""
    ts = time.strftime('%s')
    path = f'scraped_memes_{ts}.csv'

    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for meme in memes:
            writer.writerow([meme.name, meme.url])
    print(f'Memes written to {path}!')

def read_scraped_memes(path: str) -> list:
    memes = []
    with open(path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            meme = Meme(row[0], row[1])
            memes.append(meme)
    return memes
        

if __name__ == "__main__":
    html = read_html(sys.argv[1])
    soup = get_soup(html)
    memes = scrape_memes(soup)
    if memes:
        write_scraped_memes(memes)