class Node:
    def __init__(self, val, link=None):
        self.val = val
        self.link = link

    def _valid_link(self, link):
        return isinstance(link, self.__class__) or link is None

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link):
        if not self._valid_link(link):
            raise TypeError
        self.__link = link
