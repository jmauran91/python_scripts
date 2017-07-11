
import shutil
import os
import glob
from bs4 import BeautifulSoup
import requests
import xlsxwriter

ALPHABET = list(string.ascii_uppercase)
url = raw_input("Give full URL of desired page:")
xcel_file = raw_input("Name of file you want to scrape into?")
scrape1 = raw_input("What do you want to scrape for?")
r = requests.get(url)
page_data = r.text
soup = BeautifulSoup(page_data)

workbook = xlsxwriter.Workbook(xcel_file)
worksheet = workbook.add_worksheet()

index = 1
for name in soup.get_all(scrape1):
    cell = (" {0} + {1}").format( ALPHABET[index], 1)
    worksheet.write(cell, name)
    index += 1


workbook.close()



## scrape the web for names and populate an excel spreadsheet with them
