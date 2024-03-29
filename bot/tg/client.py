import requests

from bot.tg.dc import (
    GET_UPDATES_RESPONSE_SCHEMA,
    SEND_MESSAGE_RESPONSE_SCHEMA,
    GetUpdatesResponse,
    SendMessageResponse
)


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f'https://api.telegram.org/bot{self.token}/{method}'

    def get_updates(self, offset: int = 0, timeout: int = 120) -> GetUpdatesResponse:
        url = self.get_url('getUpdates')
        response = requests.get(url=url, params={'offset': offset, 'timeout': timeout})
        return GET_UPDATES_RESPONSE_SCHEMA.load(response.json())

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        url = self.get_url('sendMessage')
        response = requests.get(url=url, params={'chat_id': chat_id, 'text': text})
        return SEND_MESSAGE_RESPONSE_SCHEMA.load(response.json())
