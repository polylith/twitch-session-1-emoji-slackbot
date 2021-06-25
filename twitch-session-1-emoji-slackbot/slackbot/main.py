import requests
from typing import Optional

from slack import RTMClient

def handle_node(node: dict) -> list:
    if node.get("type") == "emoji":
        return [node.get("name")]

    if node.get("elements") is None:
        return []

    result = []
    for child_node in node.get("elements"):
        result = result + handle_node(child_node)

    return result

@RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']

    result = []
    for block in data.get("blocks", []):
        result = result + handle_node(block)

    print(result)

    # TODO: filtear with blacklist

    if len(result) > 0:
        requests.post(
            "http://localhost:8000/internal_api/set_employee_emoji/",
            json={
                "smiley": result[-1],
                "user": data.get("user")
            }
        )



rtm_client = RTMClient(token="REPLACE_WITH_YOUR_WORKSPACE_TOKEN")
rtm_client.start()