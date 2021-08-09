import json
from abc import ABC, abstractmethod
from typing import List
from books.models import Book

import requests

class BookClass():
    title = None
    authors = None
    published_date = None
    categories = None
    average_rating = None
    ratings_count = None
    thumbnail = None

    def save_to_db(self):
        b = Book(authors=self.authors,
                 title=self.title,
                 published_date=self.published_date,
                 categories=self.categories,
                 average_rating=self.average_rating,
                 ratings_count=self.ratings_count,
                 thumbnail=self.thumbnail)
        b, created = Book.objects.update_or_create(authors=self.authors,
                                                   title=self.title,
                                                   defaults={
            'published_date':self.published_date
        })
        b.save()



class APIConnector():
    def __init__(self, q: str):
        self.q = q

    def get_book_data(self) -> List:
        api_request = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={self.q}")
        data = json.loads(api_request.content)
        j = api_request.json()
        print(data)

        book_item = BookClass()

        for i in range(len(j["items"])):
            volume_info = data["items"][i]["volumeInfo"]
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

            book_item.save_to_db()