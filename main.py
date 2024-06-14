from fastapi import FastAPI,status,HTTPException
import uvicorn
from typing import List
from schemas import BookSchema,CreateBookSchema,UpdateBookSchema
app=FastAPI()


books:list[BookSchema]=[]

# Helper Function
def GetBookByID(id):
    book=next((book for book in books if book.id==id),None)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"error":"book not found"})
    return book

@app.get('/',summary='Server Check')
def ping():
    return 'pong'

@app.post('/books',summary='Add a new book to the collection')
def AddBook(book:CreateBookSchema):
    last_book_id=books[-1].id if len(books)>0 else 0
    new_book=BookSchema(id=last_book_id+1,title=book.title,author=book.author,published_year=book.published_year)
    books.append(new_book)
    return new_book

@app.get('/books',response_model=list[BookSchema],summary='Get all the books in the book store')
def GetAllBooks():
    return books

@app.get('/books/{id}',response_model=BookSchema,summary='Get a specific book with the id')
def GetBook(id:int):
    return GetBookByID(id)


@app.delete('/books/{id}', summary='delete a specific book')
def DeleteBook(id:int):
    book=GetBookByID(id)
    books.remove(book)
    return {"data":"Book Deleted","status":status.HTTP_301_MOVED_PERMANENTLY}



# for a partial update, a patch request is more suitable
@app.patch('/books/{id}',summary='Update a book with it"s id')
def UpdateBook(id:int,fields:UpdateBookSchema):
    old_book=GetBookByID(id)
    book_index=books.index(old_book)
    updated_book=old_book.model_copy(update=fields.model_dump())
    books[book_index]=updated_book
    return updated_book



if __name__=='__main__':
    uvicorn.run('main:app',port=8000,reload=True,host='127.0.0.1')