#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#   get_url.py
#
#                   Aug/18/2018
#
# ------------------------------------------------------------------
import requests
import sys
from bs4 import BeautifulSoup
#
url = "https://aws.amazon.com/jp/certification/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",}
#
try:
    rr = requests.get(url,headers=headers)
    html = rr.content
    try:
        soup = BeautifulSoup(html, "html.parser")
        for aa in soup.find_all("a"):
            link = aa.get("href")
            name = aa.get_text()
            print(link,"\t",name)
    except Exception as ee:
        sys.stderr.write("*** error *** in BeautifulSoup ***\n")
        sys.stderr.write(str(ee) + "\n")
#

except Exception as ee:
    sys.stderr.write("*** error *** in requests.get ***\n")
    sys.stderr.write(str(ee) + "\n")
#
# ------------------------------------------------------------------
# ------------------------------------------------------------------