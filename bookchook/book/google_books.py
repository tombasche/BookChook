import requests


class GoogleBook:

    def __init__(self, isbn):
        self.url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'
        self.isbn = isbn

        resp = requests.get(self.url.format(self.isbn))
        try:
            resp.raise_for_status()
        except Exception as ex:
            print(ex)
            raise
        resp = resp.json()['items'][0]
        self.title = resp['volumeInfo']['title']
        self.author = ','.join(resp['volumeInfo']['authors'])
        self.description = resp['volumeInfo']['description']
        self.image = resp['volumeInfo']['imageLinks']['thumbnail']

