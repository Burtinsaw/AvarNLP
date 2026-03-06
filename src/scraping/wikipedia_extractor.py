"""Extract parallel data from Avar and Turkish Wikipedia articles."""

import httpx
from src.data_types import SentencePair


def fetch_avar_wikipedia_titles(limit: int = 500) -> list[dict]:
    """Fetch Avar Wikipedia article titles and their Turkish interwiki links."""
    url = "https://av.wikipedia.org/w/api.php"
    titles_with_links = []
    apcontinue = None

    client = httpx.Client(timeout=30.0)

    while len(titles_with_links) < limit:
        params = {
            "action": "query",
            "generator": "allpages",
            "gaplimit": 50,
            "prop": "langlinks",
            "lllang": "tr",
            "lllimit": 50,
            "format": "json",
        }
        if apcontinue:
            params["gapcontinue"] = apcontinue

        resp = client.get(url, params=params)
        data = resp.json()

        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            av_title = page.get("title", "")
            langlinks = page.get("langlinks", [])
            for ll in langlinks:
                if ll.get("lang") == "tr":
                    titles_with_links.append({"av_title": av_title, "tr_title": ll["*"]})

        if "continue" in data:
            apcontinue = data["continue"].get("gapcontinue")
        else:
            break

    client.close()
    return titles_with_links[:limit]


def extract_parallel_titles(title_pairs: list[dict]) -> list[SentencePair]:
    """Convert title pairs to SentencePairs."""
    return [
        SentencePair(
            av=item["av_title"],
            tr=item["tr_title"],
            source="wikipedia",
            quality=0.7,
        )
        for item in title_pairs
        if item["av_title"].strip() and item["tr_title"].strip()
    ]
