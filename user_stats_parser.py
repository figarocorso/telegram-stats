import re

from bs4 import BeautifulSoup

from message import Message


class UserStatsParser:

    def __init__(self):
        self.user_stats = {}
        self.last_message_user = ''

    def process_file(self, file_location):
        with open(file_location, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')

        messages = []
        soup_messages = soup.find_all(id=re.compile(r"message\d+"))
        for soup_message in soup_messages:
            messages.append(Message(soup_message))

        for message in messages:
            print("%s (%s): %s" % (message.author, message.type, message.text))

        print(len(messages))
