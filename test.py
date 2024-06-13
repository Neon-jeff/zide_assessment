from fastapi.testclient import TestClient
from schemas import BookSchema,CreateBookSchema,UpdateBookSchema
from main import app
import json


client=TestClient(app)
test_book_list:list[BookSchema]=[
    BookSchema(id= 1,
    title= "New Book",
    author= "Jeff Neon",
    published_year= 1824),
    BookSchema(id= 2,
    title= "Zide Manual",
    author= "Zide admin",
    published_year= 1824),
]

def test_add_new_book():
    response=client.post(
            '/books',
            content=json.dumps({"title":"Zide GUI Handbook","author":"Zide Admin","published_year":2000}))
    assert response.status_code==200
    # assert response.json()=={"title":"Zide GUI Handbook","author":"Zide Admin","published_year":2000}
def test_invalid_date():
    response=client.post(
            '/books',
            content=json.dumps({"title":"Zide GUI Handbook","author":"Zide Admin","published_year":1600}))
    assert response.status_code==422
    pass

def test_get_all_books():
    response=client.get('/books')
    assert response.status_code==200


def test_get_single_book_id():
    response=client.get('/books/4')
    assert response.status_code==404 or response.status_code==200

def update_book():
    response=client.patch('/books/2',data={'title':"Second book updated",'author':"Zide People"})
    assert response.status_code==200
    assert response.json()=={
    "id": 2,
    "title": "Second Book Updated",
    "author": "Zide Library",
    "published_year": 1820
}


