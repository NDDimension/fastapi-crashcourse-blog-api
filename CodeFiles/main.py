"""
Breakdown + Path Parameter demo

This module exposes three simple FastAPI endpoints to illustrate:
- GET /                  -> return a placeholder "blog list"
- GET /blog/{id}         -> return a blog detail by an integer path parameter
- GET /blog/{id}/comments-> return comments for a given blog id (id untyped here)
"""

from fastapi import FastAPI

# Create a FastAPI application instance.
# This 'app' will hold our routes (aka "path operations").
app = FastAPI()


@app.get("/")
def index():
    """
    Root endpoint.

    Returns:
        dict: JSON payload with a simple message indicating a blog list.
              FastAPI automatically serializes Python dicts to JSON and
              returns HTTP 200 by default.
    """
    # Any dict you return is serialized to JSON by FastAPI.
    # Default status code: 200 OK
    return {"data": "blog list"}


@app.get("/blog/{id}")
def show_blog(id: int):
    """
    Get details for a single blog by its ID.

    Args:
        id (int): Path parameter captured from the URL, validated as an integer.
                  If a non-integer is provided (e.g., /blog/abc), FastAPI returns
                  a 422 Unprocessable Entity error.

    Returns:
        dict: JSON payload including the requested blog ID.
    """
    # Note: The name inside { } in the route must match the function parameter name.
    # Here, 'id' is type-hinted as int, so FastAPI validates and converts it.
    return {"data": {"blog detail": id}}


@app.get("/blog/{id}/comments")
def show_comments(id):
    """
    Get comments for a blog.

    Note:
        - 'id' is intentionally left untyped here. FastAPI treats it as a string
          in OpenAPI docs since there is no type hint.
        - The value {"1", "2"} is a Python set. Sets are not directly JSON-serializable,
          but FastAPI will encode them as a list (e.g., ["1", "2"]) automatically.
          Set order is not guaranteed, so the response order may vary.
    """
    # Because 'id' has no type hint, it will be handled as a string in docs.
    # Returning a set is okay; FastAPI will json-encode it as a list.
    return {"data": {"blog comments": {"1", "2"}}}


##################################################
"""Quick explanation (what’s happening)

    - app = FastAPI(): Boots the app and registers your endpoints.
    - @app.get("/"): Declares a GET route at /. Returns a JSON dict.
    - @app.get("/blog/{id}"): Declares a GET route with a typed path param id: int. Invalid types trigger 422.
    - @app.get("/blog/{id}/comments"): Another GET route. id is untyped → treated as string in docs/validation. 
                                                            Returns a set, which FastAPI converts to a JSON list."""
