import re

from bs4 import BeautifulSoup


class UserStatsParser:

    def __init__(self):
        self.user_stats = {}
        self.last_message_user = ''

    def process_file(self, file_location):
        with open(file_location, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
        messages = soup.find_all(id=re.compile("message+\d"))
        for message in messages:
            self.process_message(message)

    def process_message(self, message):
        pass
