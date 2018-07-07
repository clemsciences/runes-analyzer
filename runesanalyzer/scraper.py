"""

"""

import time
import json
from lxml import html
import requests

from runesanalyzer.data import sweden_runic_inscription_filename

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


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
    retrieve_sweden_runic_inscription()
    sweden_runic_inscription_filename()
