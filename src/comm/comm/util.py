

def parse_topic_and_type(topic_names_and_types)->dict:
    result = {}
    for topic, types in topic_names_and_types:
        new_topic = topic[1:]
        result[new_topic] = types
    return result