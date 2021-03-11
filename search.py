import os
import requests
import gspread
import sys
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials
#
url = "https://aws.amazon.com/jp/certification/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",}

# 利用する API を指定する
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials_file = 'search-307308-cde82f148ceb.json'
path = os.path.expanduser("/Users/tsudashouki/Desktop/search/search-307308-cde82f148ceb.json")

spread_sheet_name = "search"

credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
gc = gspread.authorize(credentials)
wks = gc.open(spread_sheet_name).sheet1

try:
    rr = requests.get(url,headers=headers)
    html = rr.content
    try:
        soup = BeautifulSoup(html, "html.parser")
        for aa in soup.find_all("a"):
            link = aa.get("href")
            name = aa.get_text()
            print(link,"\t",name)
        for index, e in enumerate(link):
            num = index + 1
            wks.update_acell('A'+str(num) , e.get_text())
        for index, e in enumerate(name):
            num = index + 1
            wks.update_acell('A'+str(num) , e.get_text())

    except Exception as ee:
        sys.stderr.write("*** error *** in BeautifulSoup ***\n")
        sys.stderr.write(str(ee) + "\n")
#

except Exception as ee:
    sys.stderr.write("*** error *** in requests.get ***\n")
    sys.stderr.write(str(ee) + "\n")