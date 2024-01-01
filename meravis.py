import requests
from bs4 import BeautifulSoup, ResultSet, SoupStrainer

import config.config as cfg


def scan_site():
    r = requests.get('https://www.meravis.de/mieten/wohnungssuche')
    soup = BeautifulSoup(r.text)
    findings = soup.find_all("div", {"class": "immo-list-teaser"})
    filtered = filter_results(findings)
    prettified_results = prettify_results(filtered)
    if prettified_results == "":
        return f'Keine Wohungen in {cfg.SEARCH_LOCATION} gefunden'
    else:
        return prettified_results

def filter_results(rs: ResultSet):
    filtered = ResultSet(SoupStrainer())
    for finding in rs:
        if (cfg.SEARCH_LOCATION.lower() in str(finding.text).lower()):
            filtered.append(finding)
    return filtered


def prettify_results(rs: ResultSet):
    out = ""
    for finding in rs:
        out += str(finding.get_text("\n", True))
        link_pre = str(finding).split("href=\"")
        link_post = link_pre[1].split("\">")
        out += "\nhttps://www.meravis.de" + str(link_post[0])
        out += "\n-----------------\n"
    print(out)
    return out