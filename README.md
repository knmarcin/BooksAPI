# <center>BooksApi</center>

Api was designed to connect with Google Books API and receive data about dataset of books - and save it (or update if exists) in inner database.
<hr>

## <center>Endpoints</center>

* **GET**

    * /books - List of all saved books in database, with functionality to
    * /books?published_date=1995 - filter by published_date 
    * /books?sort=-published_date - sort by published date 
    * /books?author="J.R.R Tolkien"&author="C.S Lewis" - books from authors
    * /books/<bookId> - choosen book by id
    

* **POST** /db {"q": "Hobbit"}
    * getting dataset from https://www.googleapis.com/books/v1/volumes?q=Hobbit
    saving or updating existing to database.
      
<hr>

## <center>Requirements</center>

App was written in Django Rest Framework.

If you need to run it, you need to:
* create a virtual environment for Python 3.9.5
* install dependencies from requirements.txt file.


<hr>

## <center>Hosting</center>


<center> Currently app is hosted on Heroku, with DEBUG = TRUE mode.
https://testbooks-api.herokuapp.com </center>


<hr>