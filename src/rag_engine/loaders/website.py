import requests
from bs4 import BeautifulSoup


class WebsiteLoader:

    def load(self, url):

        response = requests.get(
            url,
            timeout=30
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup(
            ["script","style"]
        ):
            tag.decompose()

        return soup.get_text(
            " ",
            strip=True
        )
