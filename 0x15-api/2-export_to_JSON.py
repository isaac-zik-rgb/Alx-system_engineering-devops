#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import sys
from security import safe_requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_response = safe_requests.get(url + "users/{}".format(user_id))
    todos = safe_requests.get(url + "todos", params={"userId": user_id}).json()
    user = user_response.json()
    user_id = user.get("id")
    username = user.get("username")
    users_info = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]
    }
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(users_info, json_file)
