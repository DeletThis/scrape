import re

INVALID_CHARS = ["'", '"', ',', '.', '!', '?', '(', ')']
class Meme:
    """Stores the name and url of a meme."""

    def __init__(self, name=None, url=None):
        for ch in INVALID_CHARS:
            if ch in name:
                name = name.replace(ch, '')
        self.name = name
        self.url = url
    
    def get_sanitized_name(self) -> str:
        """Returns a string that *could be* a valid file name."""
        #  (data.h2.get_text(strip=True).split('/')[0].replace(",|:",""), data.a['href'])
        return self.name

    def is_alphanumspace(self) -> bool:
        return re.match(r'^[A-Za-z0-9 _-]*$', self.name)