from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from logic.fruit import get_fruit
from logic.wiki import wiki_search, wiki_page, wiki_keywords


app = FastAPI()


class Wiki(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello FastAPI"}


@app.get("/fruit")
async def fruit():
    """Use a library to get a random fruit"""

    return {"fruit": get_fruit()}


@app.post("/search")
async def search(wiki: Wiki):
    """Search Wikipedia for a name

    Parameters
    ----------
    wiki : Wiki
        A Wiki object with a name attribute
    returns : list
    """

    return wiki_search(wiki.name)


@app.post("/page")
async def page(wiki: Wiki):
    """Get a page from Wikipedia
    Parameters
    ----------
    wiki : Wiki
        A Wiki object with a name attribute
    returns : dict
    """

    return wiki_page(wiki.name)


@app.post("/keywords")
async def keywords(wiki: Wiki):
    """Get keywords from Wikipedia
    Parameters
    ----------
    wiki : Wiki
        A Wiki object with a name attribute
    returns : list
    """

    return wiki_keywords(wiki.name)


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together using URL Parameters and a GET

    This is one way to capture input from a user or API
    """

    total = num1 + num2
    return {"total": total}


if __name__ == "__main__":
    print("I was here")
    uvicorn.run(app, port=8080, host="0.0.0.0")
