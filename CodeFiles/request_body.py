"""
Query Parameters + Request Body demo (Bitfumes)

Endpoints:
- GET  /blog
    Query params:
      * limit: int = 10
      * published: bool = True
      * sort: Optional[str] = None
- GET  /blog/unpublished
- GET  /blog/{id}
- GET  /blog/{id}/comments
- POST /blog
    JSON body (Pydantic model: Blog):
      * title: str
      * body: str
      * published: Optional[bool]   # accepts True/False or null

Notes:
- Query parameters are read from the URL (after ?), not the body.
- Request body (POST /blog) is parsed from JSON into a Pydantic model (Blog),
  validated, and documented automatically in Swagger UI (/docs).
"""

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    """
    List blogs with optional filtering and sorting.

    Query Parameters:
        limit (int, default 10): Maximum number of blogs to return.
        published (bool, default True): If True, only return published blogs.
        sort (Optional[str], default None): Sort order or key (e.g., "asc", "desc").

    Behavior:
        - FastAPI will parse and validate query params by type hints.
        - Invalid types produce a 422 validation error response.
    """
    # Examples:
    #   /blog?limit=5&published=false&sort=asc
    #   /blog?limit=20                    -> uses defaults for others
    if published:
        return {"data": f"{limit} published blogs from db.", "sort": sort}
    else:
        return {"data": f"{limit} blogs from db.", "sort": sort}


@app.get("/blog/unpublished")
def unpublished():
    """
    Return a static list of unpublished blogs.

    Tip:
        You could alternatively use /blog?published=false to filter via query params.
        Having a dedicated route is a design choice for clarity or caching.
    """
    return {"data": "unpublished blog list"}


@app.get("/blog/{id}")
def show_blog(id: int):
    """
    Retrieve a specific blog by its ID.

    Path Parameters:
        id (int): Validated as integer; non-integers will raise a 422 error.
    """
    return {"data": {"blog detail": id}}


@app.get("/blog/{id}/comments")
def show_comments(id):
    """
    Retrieve comments for a given blog.

    Notes:
        - 'id' has no type hint here, so it will be treated as string in docs.
        - Returning a Python set {"1", "2"} is not JSON-native; FastAPI encodes it to a list.
          Ordering is not guaranteed because sets are unordered.
    """
    return {"data": {"blog comments": {"1", "2"}}}


class Blog(BaseModel):
    """
    Pydantic model describing the expected request body for POST /blog.

    Fields:
        title (str): Blog title (required).
        body (str): Blog content/body (required).
        published (Optional[bool]): May be True/False or null (None).

    Important:
        Optional[bool] here means "the value can be None", but the field is still
        required by default unless you give it a default value (e.g., = None).
        If you want 'published' to be optional and omitted, declare:
            published: bool | None = None
    """

    title: str
    body: str
    published: Optional[bool]  # accepts null; still required unless default is provided


@app.post("/blog")
def create_blog(blog: Blog):
    """
    Create a new blog from a JSON request body.

    Body:
        blog (Blog): Parsed and validated from the JSON payload.
            Example:
            {
                "title": "My first post",
                "body": "Hello world",
                "published": true
            }

    Returns:
        dict: Confirmation message.

    Notes:
        - By default, this returns HTTP 200. For a proper "create", use status_code=201.
        - Validation errors (missing/invalid fields) produce HTTP 422 with details.
    """
    # FastAPI automatically:
    # 1) Reads JSON from the request body (Content-Type: application/json).
    # 2) Validates & parses it into the Blog model.
    # 3) Injects the model instance into this function as 'blog'.
    return {"data": f"Blog created with title {blog.title} and body {blog.body}"}
