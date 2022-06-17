from pydantic import BaseSettings
from os import path

class PublisherSettings(BaseSettings):
    topic_name: str
    time_period:int


class SubscriberSettings(BaseSettings):
    topic_name: str
    class Config:
        env_file = path.join(path.dirname(__file__),'subscriber.env')
        env_file_encoding = 'utf-8'

class ServiceSettings(BaseSettings):
    service_name:str

publisher_setting = PublisherSettings(_env_file = path.join(path.dirname(__file__),"..","config",'publisher_and_subscriber.env'))
subscriber_setting = SubscriberSettings(_env_file = path.join(path.dirname(__file__),"..","config",'publisher_and_subscriber.env'))
service_setting = ServiceSettings(_env_file = path.join(path.dirname(__file__),"..","config",'service.env'))

# publisher_setting = PublisherSettings()
# subscriber_setting = SubscriberSettings()
# service_setting = ServiceSettings()