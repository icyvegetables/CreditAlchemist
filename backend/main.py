from typing import Union
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb+srv://codefest:codefest2025@cluster0.efpl4.mongodb.net/")
db = client["data"]

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, Union[int, Union[str, None]]]:
    """
    Endpoint to read an item by its ID.

    Args:
        item_id (int): The ID of the item.
        q (str, optional): An optional query parameter.

    Returns:
        dict: A dictionary containing the item ID and the query parameter.
    """
    return {"item_id": item_id, "q": q}


@app.get("/cc")
def get_credit_cards() -> list[dict]:
    """
    Endpoint to get all credit cards.

    Returns:
        list: a list of all credit cards.
    """

    credit_cards_list = []
    for credit_card in db["cc_info"].find({}, {"_id": 0}):
        credit_cards_list.append(credit_card)
    return credit_cards_list


@app.get("/chats")
def get_chats():
    """
    Endpoint to get all chat sessions.

    Returns:
        dict: A dictionary containing a list of all chat sessions.
    """
    chats = db["chat_sessions"].find()
    print(list(chats))
    return {"chats": list(chats)}

@app.post("/chats")
def create_chat():
    """
    Endpoint to create a new chat session.

    Returns:
        dict: A dictionary containing the ID of the created chat session.
    """
    chat_id = db["chat_sessions"].insert_one({}).inserted_id
    return {"chat_id": str(chat_id)}

@app.get("chats/{chat_id}/messages")
def get_chat_history(chat_id: str):
    """
    Endpoint to get the chat history of a specific chat session.

    Args:
        chat_id (str): The ID of the chat session.

    Returns:
        dict: A dictionary containing the chat history of the specified session.
    """
    history = db["chat_history"].find({"SessionId": chat_id})
    print(list(history))
    return {"history": list(history)}

@app.post("chats/{chat_id}")
def name_session(chat_id: str, name: str):
    """
    Endpoint to name a chat session.

    Args:
        chat_id (str): The ID of the chat session.
        name (str): The name to be assigned to the chat session.

    Returns:
        dict: A dictionary indicating the status of the operation.
    """
    db["chat_sessions"].update_one({"_id": chat_id}, {"$set": {"name": name}})
    return {"status": "ok"}

@app.delete("chats/{chat_id}")
def delete_session(chat_id: str):
    """
    Endpoint to delete a chat session and its history.

    Args:
        chat_id (str): The ID of the chat session.

    Returns:
        dict: A dictionary indicating the status of the operation.
    """
    db["chat_sessions"].delete_one({"_id": chat_id})
    db["chat_history"].delete_many({"SessionId": chat_id})
    return {"status": "ok"}

@app.post("chats/{chat_id}/messages")
def send_message(chat_id: str, message: str):
    """
    Endpoint to send a message in a chat session.

    Args:
        chat_id (str): The ID of the chat session.
        message (str): The message to be sent.

    Returns:
        dict: A dictionary indicating the status of the operation.
    """
    # placeholder for sending message
    return {"status": "message sent"}