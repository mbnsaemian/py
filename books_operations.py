books=[]

def add_book():
    global books 
    book ={}
    book["title"] = input("enter title of the book : ")
    book["author"] = input("enter author of the book : ")
    book["pages"] = int(input("enter number of pages : "))
    book["price"] = float(input("enter price of the book : "))
    book["ISBN"] = input("enter ISBN of the book : ")
    books.append(book)
 

def  list_books():
     for book in books :
       print(f"title of book : {book['title']}")
       print(f"author of book :{book['title']}")
       print(f"number of pages :{book['pages']}")
       print(f"price of book :{book['price']}")
       print(f"ISBN of book:{book['ISBN']}")
       print("-------------------------------------------------")

def find_book():
    ISBN = input("enter ISBN to find a book : ")
    for book in books :
       if book["ISBN"] == ISBN :
            print(f"title of book : {book['title']}")
            print(f"author of book :{book['title']}")
            print(f"number of pages :{book['pages']}")
            print(f"price of book :{book['price']}")
            print(f"ISBN of book:{book['ISBN']}")
            print("-------------------------------------------------")            
            break
    else :
          print("this book is not in books database")
       
def delete_book():
    ISBN = input("enter ISBN to delete a book :")
    for book in books :
       if book["ISBN"] == ISBN :
          books.remove(book)
          print("the book has been delete sucvecssfully")
