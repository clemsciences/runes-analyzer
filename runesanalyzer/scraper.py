import time
import json
from lxml import html
import requests

from runesanalyzer.data import sweden_runic_inscription_filename
# site = "http://christerhamp.se/runor/gamla/index.html"
# extract all links in the web page which starts with "http://christerhamp.se/runor/gamla/"

# extract the transliterated inscriptions : p[class="trans"]
# extract the region of the inscription
# ----------------------------------------------------------
site = "http://runes.verbix.com/index.html"


def retrieve_sweden_runic_inscription():
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


