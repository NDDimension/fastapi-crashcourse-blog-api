"""
Query Parameters demo (Bitfumes)

This module shows how to work with query parameters in FastAPI:
- GET /blog?limit=10&published=true&sort=asc
  * limit: int (default 10)
  * published: bool (default True)
  * sort: Optional[str] (e.g., "asc" or "desc")
- Also includes a static route (/blog/unpublished) and path-param routes.
"""

from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    """
    List blogs with optional filtering and sorting via query parameters.

    Query Parameters:
        limit (int, default 10): Max number of blogs to return.
        published (bool, default True): If true, return only published blogs.
        sort (str | None, optional): Sorting order or key (e.g., "asc", "desc").

    Notes:
        - Type hints drive parsing and validation:
          * non-integer limit -> 422 Unprocessable Entity
          * published parses from strings like "true"/"false" (case-insensitive)
        - Optional[str] with default None means parameter is optional.
    """
    # FastAPI converts query strings to typed Python values based on annotations.
    # Examples:
    #   /blog?limit=5&published=false&sort=asc
    #       -> limit=5 (int), published=False (bool), sort="asc" (str)
    if published:
        return {"data": f"{limit} published blogs from db.", "sort": sort}
    else:
        return {"data": f"{limit} blogs from db.", "sort": sort}


@app.get("/blog/unpublished")
def unpublished():
    """
    Explicit endpoint for unpublished blogs.

    Tip:
        You can also use /blog?published=false to filter unpublished via query params.
        This dedicated path is useful if you want a stable, descriptive route.
    """
    return {"data": "unpublished blog list"}


@app.get("/blog/{id}")
def show_blog(id: int):
    """
    Retrieve a specific blog by ID.

    Path Parameters:
        id (int): Captured from the URL and validated as an integer.
    """
    return {"data": {"blog detail": id}}


@app.get("/blog/{id}/comments")
def show_comments(id):
    """
    Retrieve comments for a given blog.

    Note:
        - 'id' is untyped (treated as string in docs).
        - Returning a set {"1", "2"} is okay; FastAPI serializes it to a list.
          Ordering of sets is not guaranteed, so response order may vary.
    """
    return {"data": {"blog comments": {"1", "2"}}}


"""What’s happening (quickly)

    - Query params live after ? and are separated by &: /blog?limit=10&published=true&sort=asc
    - FastAPI reads them into function parameters that aren’t part of the path.
    - Type hints (int, bool, Optional[str]) give you parsing + validation for free:
    - Invalid types → 422 with a descriptive error.
    - Static route /blog/unpublished coexists safely with /blog/{id}; static paths win when there’s overlap."""
