#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user["username"]
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.json".format(user_id), 'w') as json_file:

        json.dump({user_id: [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": username} for task in todos]},
                  json_file)
