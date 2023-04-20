import os


class parameters:

    def __init__(self):
        self._baseURI = "https://api.tmsandbox.co.nz"

    def get_baseURI(self):
        if os.getenv('baseURI') is not None:
            self._baseURI = os.getenv('baseURI')
        return self._baseURI

    def st_baseURI(self, x):
        self._baseURI = x

    baseURI = property(get_baseURI, st_baseURI)

