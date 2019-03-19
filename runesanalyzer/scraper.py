"""

Main page: https://www.nordiska.uu.se/forskn/samnord.htm/?languageId=1
Data archive: www.runforum.nordiska.uu.se/filer/srd2014.zip
License: https://opendatacommons.org/licenses/odbl/1.0/
loggbok: http://www.runforum.nordiska.uu.se/filer/loggbok_2008-2014.pdf
"""

import os
import time
import json
from lxml import html
import requests
import zipfile
import codecs

from runesanalyzer.data import sweden_runic_inscription_filename

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def retrieve_scandinavian_runic_text_database():
    """

    :return:
    """
    data = requests.get("http://www.runforum.nordiska.uu.se/filer/srd2014.zip")
    with open("data.zip", "wb") as f:
        f.write(data.content)

    zip_ref = zipfile.ZipFile("data.zip", 'r')
    zip_ref.extractall("data_runes")
    zip_ref.close()


def read_fornspr():
    return {}


def read_fornnsprx():
    return {}


def read_fvn():
    return {}


def read_fvnx():
    return {}


def read_litt():
    return {}


def read_runtext():
    return {}


def read_runtextx():
    return {}


def retrieve_sweden_runic_inscription():
    site = "http://runes.verbix.com/index.html"
    rrunes = requests.get(site)
    tree = html.fromstring(rrunes.text)
    links = [i.get("href") for i in tree.xpath("//a") if "vikingage" in i.get("href")]
    runes = {}
    for link in links:
        page = requests.get("http://runes.verbix.com/"+link)
        tree = html.fromstring(page.text)
        rune_blocks = tree.xpath('//p[@class="rrune"]')
        print(len(rune_blocks))
        content = [rb.text for rb in rune_blocks]
        runes[link] = content
        print(content)
        time.sleep(1)
    with open("sweden_runes.json", "w") as f:
        json.dump(runes, f)

    with open("sweden_runes.json", "r") as f:
        loaded_runes = json.load(f)

    print(loaded_runes.keys())


if __name__ == "__main__":
    # retrieve_sweden_runic_inscription()
    # sweden_runic_inscription_filename()
    # retrieve_scandinavian_runic_text_database()
    print(read_rundata()[:10])
