import json
from books.models import Book

import requests

#TODO Consider using dataclasses, which may look like this. This gives you validation you are looking for.

from dataclasses import dataclass


@dataclass
class BookDataclass:
    google_id: int = None
    title: str = None


class BookClass:
    google_id = None
    title = None
    authors = None
    published_date = None
    categories = None
    average_rating = None
    ratings_count = None
    thumbnail = None

    def save_to_db(self):
        #TODO Naming convention should be more explicit. I guess `b` stands for book.
        b, created = Book.objects.update_or_create(google_id=self.google_id,
                                                   defaults={
                                                       'authors': self.authors,
                                                       'title': self.title,
                                                       'published_date': self.published_date,
                                                       'average_rating': self.average_rating,
                                                       'ratings_count': self.ratings_count,
                                                       'thumbnail': self.thumbnail,
                                                       'categories': self.categories
                                                   })
        b.save()


class APIConnector:
    def __init__(self, q: str):
        #TODO Again naming convention
        self.q = q

    def get_book_data(self):
        api_request = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={self.q}")
        data = json.loads(api_request.content)
        j = api_request.json()

        book_item = BookClass()

        for i in range(len(j["items"])):
            volume_info = data["items"][i]["volumeInfo"]
            #TODO Simply do:
            book_item.authors = volume_info.get("authors") # if it's going to be none then it will pass none,
            # no error will appear. Plus you don't have to deal with try-except.
            try:
                book_item.authors = volume_info["authors"]
            except:
                pass
            try:
                book_item.title = volume_info['title']
            except:
                pass
            try:
                book_item.published_date = volume_info['publishedDate'][:4]
            except:
                pass
            try:
                book_item.categories = volume_info['categories']
            except:
                pass
            try:
                book_item.average_rating = volume_info['averageRating']
            except:
                pass
            try:
                book_item.ratings_count = volume_info['ratingsCount']
            except:
                pass
            try:
                book_item.thumbnail = volume_info['imageLinks']['thumbnail']
            except:
                pass
            try:
                book_item.google_id = data["items"][i]["id"]
            except:
                pass

            try:
                book_item.save_to_db()
            except:
                pass
