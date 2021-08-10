# BooksApi

Api was designed to connect with Google Books API and receive data about dataset of books - and save it (or update if exists) in inner database.

## Endpoints

GET
* books - List of all saved books in database, with functionality to
* filter by published_date /books?published_date=1995
* sort by published date /books?sort=-published_date
* /books?author="J.R.R Tolkien"&author="C.S Lewis" - books from authors
* /books/<bookId> - choosen book by id

POST /db {"q": "Hobbit"} 
* getting dataset from https://www.googleapis.com/books/v1/volumes?q=Hobbit
saving or updating existing to database.

## Requirements

App was written in Django Rest Framework.

If you need to run it, you need to:
* create a virtual environment for Python 3.9.5
* install dependencies from requirements.txt file.

## Hosting

Currently app is hosted on Heroku
https://testbooks-api.herokuapp.com