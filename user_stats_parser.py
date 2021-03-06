import re

from bs4 import BeautifulSoup

from message import Message


class UserStatsParser:

    def __init__(self):
        self.user_stats = {}
        self.last_message_user = ''
        self.messages = []

    def process_file(self, file_location):
        with open(file_location, 'r', encoding='utf-8', errors='replace') as f:
            soup = BeautifulSoup(f, 'html.parser')

        soup_messages = soup.find_all(id=re.compile(r"message\d+"))
        for soup_message in soup_messages:
            self.messages.append(Message(soup_message))
