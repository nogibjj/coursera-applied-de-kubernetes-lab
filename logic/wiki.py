import wikipedia
import yake


def wiki_search(name):
    """Search Wikipedia for a name"""

    return wikipedia.search(name)


def wiki_page(name):
    """Get a page from Wikipedia"""

    payload = {
        "title": name,
        "summary": wikipedia.summary(name),
        "url": wikipedia.page(name).url,
    }
    return payload


def wiki_keywords(name):
    """Get keywords from Wikipedia"""

    return yake.KeywordExtractor().extract_keywords(wikipedia.summary(name))
