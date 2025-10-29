from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Initialize FastAPI application
app = FastAPI()


class Tea(BaseModel):
    """
    Data model for a Tea item.

    Attributes:
        id (int): Unique identifier for each tea.
        name (str): Name of the tea.
        origin (str): Country or region where the tea comes from.
    """

    id: int
    name: str
    origin: str


# In-memory "database" (list) to store tea objects
teas: List[Tea] = []


@app.get("/")
def read_route():
    """
    Root route that returns a welcome message.

    Returns:
        dict: A simple JSON message.
    """
    return {"message": "Welcome to Tea House"}


@app.get("/teas")
def get_teas():
    """
    Retrieve all teas from the in-memory database.

    Returns:
        list: List of all tea objects.
    """
    return teas


@app.post("/teas")
def add_tea(tea: Tea):
    """
    Add a new tea to the collection.

    Args:
        tea (Tea): The tea object to be added.

    Returns:
        dict: Success message and the added tea.
    """
    teas.append(tea)  # Add tea to in-memory list
    return {"message": "Tea added successfully", "tea": tea}


@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    """
    Update an existing tea by its ID.

    Args:
        tea_id (int): The ID of the tea to be updated.
        updated_tea (Tea): The new tea object with updated details.

    Returns:
        dict: Success message and updated tea, or error if not found.
    """
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return {"message": "Tea updated successfully", "tea": updated_tea}
    return {"error": "Tea not found"}


@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    """
    Delete a tea from the collection by its ID.

    Args:
        tea_id (int): The ID of the tea to delete.

    Returns:
        dict: Success message and deleted tea, or error if not found.
    """
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)  # Remove tea from list
            return {"message": "Tea deleted successfully", "tea": deleted}
    return {"error": "Tea not found"}
