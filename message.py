AUTHOR_SELECTOR = '.from_name'
TEXT_SELECTOR = '.text'
PHOTO_SELECTOR = '.photo'


class Message:

    def __init__(self, soup_message):
        self.soup_message = soup_message
        self.author = self.parse_author()
        self.type = self.parse_message_type()
        self.text = self.parse_text()

    def parse_author(self):
        author = self.soup_message.select_one(AUTHOR_SELECTOR)
        author = author.text if author is not None else ''
        return self.clean_text(author)

    def parse_message_type(self):
        if self.soup_message.select_one(TEXT_SELECTOR) is not None:
            return 'text'
        if self.soup_message.select_one(PHOTO_SELECTOR) is not None:
            return 'photo'
        return ''

    def parse_text(self):
        text_element = self.soup_message.select_one(TEXT_SELECTOR)
        if text_element is not None:
            return self.clean_text(text_element.text)
        return ''

    def clean_text(self, text):
        return text.rstrip().lstrip()
