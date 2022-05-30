import requests

HOST = "https://00d5-36-236-186-233.jp.ngrok.io"

def post_to_content(body) -> requests.Response:
    return requests.post(
        url=f"{HOST}/content",
        headers={"Content-Type": "application/json"},
        data=body
    )

def parse_topic_and_type(topic_names_and_types)->dict:
    result = {}
    for topic, types in topic_names_and_types:
        new_topic = topic[1:]
        result[new_topic] = types
    return result