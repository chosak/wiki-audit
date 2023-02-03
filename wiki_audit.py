import csv
import re
import sys
from datetime import datetime
from urllib.parse import urlparse

import click
import httpx
from bs4 import BeautifulSoup


def get_root_url(url):
    parts = urlparse(url)
    return f"{parts.scheme}://{parts.netloc}"


def get_html(url):
    response = httpx.get(url)
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    return response.text


def get_page_urls(html):
    soup = BeautifulSoup(html, "html.parser")
    pages_box = soup.find("div", {"id": "wiki-pages-box"})
    for li in pages_box.findAll("li"):
        if link := li.find("a"):
            yield link["href"]


def make_absolute(root_url, url):
    return url if url.startswith("http") else f"{root_url}://{url}"

def generate_url_images(url):
    root_url = get_root_url(url)
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1", {"class": "gh-header-title"}).text

    meta = soup.find("div", {"class": "gh-header-meta"})
    last_updated_str = meta.find("relative-time")["datetime"]
    last_updated = datetime.strptime(last_updated_str, "%Y-%m-%dT%H:%M:%SZ")

    page_dict = {
        "page_url": url,
        "page_title": title,
        "page_last_updated": last_updated,
    }

    content = soup.find("div", {"id": "wiki-wrapper"})

    for image_tag in content.find_all("img"):
        yield {
            **page_dict,
            "image_type": "visible",
            "src": make_absolute(root_url, image_tag["src"]),
            "text": image_tag.get("alt"),
        }

    image_links = [
        link
        for link in content.find_all("a")
        if re.match(r".*\.(jpg|png|gif)$", link["href"])
    ]

    for image_link in image_links:
        yield {
            **page_dict,
            "image_type": "link",
            "src": make_absolute(root_url, image_link["href"]),
            "text": image_link.text,
        }


def generate_page_urls(url):
    root_url = get_root_url(url)
    for page_url in get_page_urls(get_html(url)):
        yield f"{root_url}{page_url}"


def generate_wiki_images(url):
    for page_url in generate_page_urls(url):
        yield from generate_url_images(page_url)


def write_dicts(rows):
    writer = None

    for row in rows:
        if writer is None:
            writer = csv.DictWriter(sys.stdout, row.keys(), csv.QUOTE_ALL)
            writer.writeheader()

        writer.writerow(row)


def write_wiki_images(url):
    return write_dicts(generate_wiki_images(url))


@click.command()
@click.argument("url", type=str, required=True)
def main(url):
    return write_wiki_images(url)
