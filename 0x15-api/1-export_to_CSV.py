#!/usr/bin/python3
"""Export data in the CSV formate"""
import csv
import sys
from security import safe_requests

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = safe_requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = safe_requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(user_id), 'w', newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow([user_id, username, task.get("completed"),
                              task.get("title")]) for task in todos]
